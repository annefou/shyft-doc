
import os
import datetime as dt
import pandas as pd
import sys
from matplotlib import pyplot as plt
from netCDF4 import Dataset

# print(os.environ['SHYFTDATA'])


from shyft import api
import shyft


from shyft.repository.netcdf.cf_geo_ts_repository import CFDataRepository
from shyft.repository.netcdf.cf_region_model_repository import CFRegionModelRepository
from shyft.repository.geo_ts_repository_collection import GeoTsRepositoryCollection
from shyft.repository.interpolation_parameter_repository import InterpolationParameterRepository
from shyft.repository.generated_state_repository import GeneratedStateRepository


def construct_geots_repo(datasets_config, epsg=None):
    """ iterates over the different sources that are provided
    and prepares the repository to read the data for each type"""
    geo_ts_repos = []
    src_types_to_extract = []
    for source in datasets_config['sources']:
        if epsg is not None:
            source['params'].update({'epsg': epsg})
        # note that here we are instantiating the different source repositories
        # to place in the geo_ts list
        geo_ts_repos.append(source['repository'](**source['params']))
        src_types_to_extract.append(source['types'])

    return GeoTsRepositoryCollection(geo_ts_repos, src_types_per_repo=src_types_to_extract)


def time_axis_from_dict(t_dict):
    utc = api.Calendar()

    sim_start = dt.datetime.strptime(t_dict['start_datetime'], "%Y-%d-%mT%H:%M:%S")
    utc_start = utc.time(
        api.YMDhms(sim_start.year, sim_start.month, sim_start.day, sim_start.hour, sim_start.minute, sim_start.second))
    tstep = t_dict['run_time_step']
    nstep = t_dict['number_of_steps']
    time_axis = api.TimeAxis(utc_start, tstep, nstep)

    return time_axis


class interp_config(object):
    """ a simple class to provide the interpolation parameters """

    def __init__(self):
        self.interp_params = {'precipitation': {'method': 'idw',
                                                'params': {'distance_measure_factor': 1.0,
                                                           'max_distance': 600000.0,
                                                           'max_members': 10,
                                                           'scale_factor': 1.02}},
                              'radiation': {'method': 'idw',
                                            'params': {'distance_measure_factor': 1.0,
                                                       'max_distance': 600000.0,
                                                       'max_members': 10}},
                              'relative_humidity': {'method': 'idw',
                                                    'params': {'distance_measure_factor': 1.0,
                                                               'max_distance': 600000.0,
                                                               'max_members': 10}},
                              #
                              'temperature': {'method': 'idw',
                                              'params': {'max_distance': 600000.0,
                                                         'max_members': 10,
                                                         'distance_measure_factor': 1.0,
                                                         'default_temp_gradient': -0.005,  # degC/m, so -0.5 degC/100m
                                                         'gradient_by_equation': False}
                                              },
                              #  'temperature': {'method': 'btk',
                              #  'params': {'nug': 0.5,
                              #   'range': 200000.0,
                              #   'sill': 25.0,
                              #   'temperature_gradient': -0.6,
                              #   'temperature_gradient_sd': 0.25,
                              #   'zscale': 20.0}},
                              'wind_speed': {'method': 'idw',
                                             'params': {'distance_measure_factor': 1.0,
                                                        'max_distance': 600000.0,
                                                        'max_members': 10}}}

    def interpolation_parameters(self):
        return self.interp_params


def region_env_from_sources(sources):
    region_env = api.ARegionEnvironment()
    region_env.temperature = sources["temperature"]
    region_env.precipitation = sources["precipitation"]
    region_env.radiation = sources["radiation"]
    region_env.wind_speed = sources["wind_speed"]
    region_env.rel_hum = sources["relative_humidity"]
    return region_env

RegionDict = {'region_model_id': 'demo', #a unique name identifier of the simulation
              'domain': {'EPSG': 32633,
                        'nx': 400,
                        'ny': 80,
                        'step_x': 1000,
                        'step_y': 1000,
                        'lower_left_x': 100000,
                        'lower_left_y': 6960000},
              'repository': {'class': shyft.repository.netcdf.cf_region_model_repository.CFRegionModelRepository,
                             'params': {'data_file': 'shyft-data/netcdf/orchestration-testdata/cell_data.nc'}},
          }

ModelDict = {'model_t': shyft.api.pt_gs_k.PTGSKModel,  # model to construct
            'model_parameters': {
                'actual_evapotranspiration':{
                    'ae_scale_factor': 1.5},
                'gamma_snow':{
                    'calculate_iso_pot_energy': False,
                    'fast_albedo_decay_rate': 6.752787747748934,
                    'glacier_albedo': 0.4,
                    'initial_bare_ground_fraction': 0.04,
                    'max_albedo': 0.9,
                    'max_water': 0.1,
                    'min_albedo': 0.6,
                    'slow_albedo_decay_rate': 37.17325702015658,
                    'snow_cv': 0.4,
                    'tx': -0.5752881492890207,
                    'snowfall_reset_depth': 5.0,
                    'surface_magnitude': 30.0,
                    'wind_const': 1.0,
                    'wind_scale': 1.8959672005350063,
                    'winter_end_day_of_year': 100},
                'kirchner':{ 
                    'c1': -3.336197322290274,
                    'c2': 0.33433661533385695,
                    'c3': -0.12503959620315988},
                'precipitation_correction': {
                    'scale_factor': 1.0},
                'priestley_taylor':{'albedo': 0.2,
                    'alpha': 1.26},
                    }
            }               


ForcingData = {'sources': [
        
    {'repository': shyft.repository.netcdf.cf_geo_ts_repository.CFDataRepository,
     'params': {'epsg': 32633,
            'selection_criteria': None,
            'stations_met': 'shyft-data/netcdf/orchestration-testdata/precipitation.nc'},
     'types': ['precipitation']},
       
    {'repository': shyft.repository.netcdf.cf_geo_ts_repository.CFDataRepository,
     'params': {'epsg': 32633,
            'selection_criteria': None,
            'stations_met': 'shyft-data/netcdf/orchestration-testdata/temperature.nc'},
    'types': ['temperature']},
        
    {'params': {'epsg': 32633,
            'selection_criteria': None,
            'stations_met': 'shyft-data/netcdf/orchestration-testdata/wind_speed.nc'},
     'repository': shyft.repository.netcdf.cf_geo_ts_repository.CFDataRepository,
     'types': ['wind_speed']},
    
    {'repository': shyft.repository.netcdf.cf_geo_ts_repository.CFDataRepository,
     'params': {'epsg': 32633,
            'selection_criteria': None,
            'stations_met': 'shyft-data/netcdf/orchestration-testdata/relative_humidity.nc'},
     'types': ['relative_humidity']},
    
    {'repository': shyft.repository.netcdf.cf_geo_ts_repository.CFDataRepository,
     'params': {'epsg': 32633,
            'selection_criteria': None,
            'stations_met': 'shyft-data/netcdf/orchestration-testdata/radiation.nc'},
     'types': ['radiation']}]
      }

TimeDict = {'start_datetime': "2013-09-01T00:00:00",
           'run_time_step': 86400, # seconds, daily
           'number_of_steps': 365 # one year
           }

region_repo = CFRegionModelRepository(RegionDict, ModelDict)

region_model = region_repo.get_region_model('demo')

geots_repo = construct_geots_repo(ForcingData)

time_axis = time_axis_from_dict(TimeDict)

bbox = region_model.bounding_region.bounding_box(region_model.bounding_region.epsg())

period = time_axis.total_period() #just defined above

# required forcing data sets we want to retrieve
geo_ts_names = ("temperature", "wind_speed", "precipitation",
                              "relative_humidity", "radiation")

sources = geots_repo.get_timeseries( geo_ts_names, period, geo_location_criteria=bbox )


region_env = region_env_from_sources(sources)


ip_conf = interp_config()
ip_repo = InterpolationParameterRepository(ip_conf)

region_model.interpolation_parameter = ip_repo.get_parameters(0) #just a '0' for now


init_values = {'gs': {'acc_melt': 0.0,
   'albedo': 0.65,
   'alpha': 6.25,
   'iso_pot_energy': 0.0,
   'lwc': 0.1,
   'sdc_melt_mean': 0.0,
   'surface_heat': 30000.0,
   'temp_swe': 0.0},
  'kirchner': {'q': 0.01}}

state_repo = GeneratedStateRepository(region_model, init_values=init_values)

# we need the state_repository to have the same size as the model
state_repo.n = region_model.size()



def runnable(reg_mod):
    """ returns True if model is properly configured 
    **note** this is specific depending on your model's input data requirements """
    return all((reg_mod.initial_state.size() > 0, reg_mod.time_axis.size() > 0))

if runnable(region_model):
    pass

interp_return = region_model.run_interpolation(region_model.interpolation_parameter, time_axis.fixed_dt, region_env)
region_model.revert_to_initial_state()
region_model.run_cells()

    


# In[85]:


region_model.revert_to_initial_state()
region_model.run_cells()


# In[92]:



# In[47]:


from matplotlib.cm import jet as jet
from matplotlib.colors import Normalize

# get all the cells for one sub-catchment with 'id' == 1228
c1228 = [c for c in region_model.cells if c.geo.catchment_id() == 1228]

# for plotting, create an mpl normalizer based on min,max elevation
elv = [c.geo.mid_point().z for c in c1228]
norm = Normalize(min(elv), max(elv))

#plot with line color a function of elevation
fig, ax = plt.subplots(figsize=(15,10))

# here we are cycling through each of the cells in c1228
for dat,elv in zip([c.env_ts.temperature.values for c in c1228], [c.mid_point().z for c in c1228]):
    ax.plot(dat, color=jet(norm(elv)), label=int(elv))
    
    
# the following is just to plot the legend entries and not related to Shyft
handles, labels = ax.get_legend_handles_labels()

# sort by labels
import operator
hl = sorted(zip(handles, labels),
            key=operator.itemgetter(1))
handles2, labels2 = zip(*hl)

# show legend, but only every fifth entry
ax.legend(handles2[::5], labels2[::5], title='Elevation [m]')


# In[39]:


# First get the time-axis which we'll use as the index for the data frame
ta = region_model.time_axis
# and convert it to datetimes
index = [dt.datetime.utcfromtimestamp(p.start) for p in ta]

# Now we'll add all the discharge series for each catchment 
data = {}
for cid in catchment_id_map:
    # get the discharge time series for the subcatchment
    q_ts = region_model.statistics.discharge([int(cid)])
    data[cid] = q_ts.values.to_numpy()

df = pd.DataFrame(data, index=index)
# we can simply use:
ax = df.plot(figsize=(20,15))
ax.legend(title="Catch. ID")
ax.set_ylabel("discharge [m3 s-1]")


# Okay, that was simple. Let's look at the timeseries in some individual cells. The following is a bit of a contrived example, but it shows some aspects of the api. We'll plot the temperature series of all the cells in one sub-catchment, and color them by elevation.

# In[69]:


from matplotlib.cm import jet as jet
from matplotlib.colors import Normalize

# get all the cells for one sub-catchment with 'id' == 1228
c1228 = [c for c in region_model.cells if c.geo.catchment_id() == 1228]

# for plotting, create an mpl normalizer based on min,max elevation
elv = [c.geo.mid_point().z for c in c1228]
norm = Normalize(min(elv), max(elv))

#plot with line color a function of elevation
fig, ax = plt.subplots(figsize=(15,10))

# here we are cycling through each of the cells in c1228
for dat,elv in zip([c.env_ts.temperature.values for c in c1228], [c.mid_point().z for c in c1228]):
    ax.plot(dat, color=jet(norm(elv)), label=int(elv))
    
    
# the following is just to plot the legend entries and not related to Shyft
handles, labels = ax.get_legend_handles_labels()

# sort by labels
import operator
hl = sorted(zip(handles, labels),
            key=operator.itemgetter(1))
handles2, labels2 = zip(*hl)

# show legend, but only every fifth entry
ax.legend(handles2[::5], labels2[::5], title='Elevation [m]')


# As we would expect from the temperature kriging method, we should find higher elevations have colder temperatures. As an exercise you could explore this relationship using a scatter plot.

# Now we're going to create a function that will read initial states from the `initial_state_repo`. In practice, this is already done by the `ConfgiSimulator`, but to demonstrate lower level functions, we'll reset the states of our `region_model`:

# In[ ]:


# create a function to read the states from the state repository
def get_init_state_from_repo(initial_state_repo_, region_model_id_=None, timestamp=None):
    state_id = 0
    if hasattr(initial_state_repo_, 'n'):  # No stored state, generated on-the-fly
        initial_state_repo_.n = region_model.size()
    else:
        states = initial_state_repo_.find_state(
            region_model_id_criteria=region_model_id_,
            utc_timestamp_criteria=timestamp)
        if len(states) > 0:
            state_id = states[0].state_id  # most_recent_state i.e. <= start time
        else:
            raise Exception('No initial state matching criteria.')
    return initial_state_repo_.get_state(state_id)
 
init_state = get_init_state_from_repo(initial_state_repo, region_model_id_=region_model_id, timestamp=region_model.time_axis.start)


# Don't worry too much about the function for now, but do take note of the `init_state` object that we created. This is another container, this time it is a class that contains `PTGSKState` objects, which are specific to the model stack implemented in the simulation (in this case `PTGSK`). If we explore an individual state object, we'll see `init_state` contains, for each cell in our simulation, the state variables for each 'method' of the method stack.
# 
# Let's look more closely:

# In[ ]:


def print_pub_attr(obj):
    #only public attributes
    print([attr for attr in dir(obj) if attr[0] is not '_']) 
    
print(len(init_state))
init_state_cell0 = init_state[0]
# gam snow states
print_pub_attr(init_state_cell0.gs)

#init_state_cell0.kirchner states
print_pub_attr(init_state_cell0.kirchner)


# #### Summary
# We have now explored the `region_model` and looked at how to instantiate a `region_model` by using a `api.ARegionEnvironment`, containing a collection of timeseries sources, and passing an `api.InterpolationParameter` class containing the parameters to use for the data interpolation algorithms. The interpolation step "populated" our cells with data from the point sources.
# 
# The cells each contain all the information related to the simulation (their own timeseries, `env_ts`; their own model parameters, `parameter`; and other attributes and methods). In future tutorials we'll work with the cells indivdual "resource collector" (`.rc`) and "state collector" (`.sc`) attributes.
# 
# 
# 
# 

# In[ ]:


fig, ax = plt.subplots(figsize=(15,10))

for pr in prec:
    t,p = [dt.datetime.utcfromtimestamp(t_.start) for t_ in pr.ts.time_axis], pr.ts.values
    ax.plot(t,p, label=pr.mid_point().x) #uid is empty now, but we reserve for later use
fig.autofmt_xdate()
ax.legend(title="Precipitation Input Sources")
ax.set_ylabel("precip[mm/hr]")



from matplotlib.cm import jet as jet
from matplotlib.colors import Normalize

# get all the cells for one sub-catchment with 'id' == 1228
c1228 = [c for c in region_model.cells if c.geo.catchment_id() == 1228]
#c1228 = region_model.cells

# for plotting, create an mpl normalizer based on min,max elevation
elv = [c.geo.mid_point().z for c in c1228]
norm = Normalize(min(elv), max(elv))


# plot with line color a function of elevation
fig, ax = plt.subplots(figsize=(15, 10))

# here we are cycling through each of the cells in c1228
for dat, elv in zip([c.env_ts.precipitation.values for c in c1228], [c.mid_point().z for c in c1228]):
    ax.plot(dat, color=jet(norm(elv)), label=int(elv))

# the following is just to plot the legend entries and not related to Shyft
handles, labels = ax.get_legend_handles_labels()

# sort by labels
import operator

hl = sorted(zip(handles, labels),
            key=operator.itemgetter(1))
handles2, labels2 = zip(*hl)

# show legend, but only every fifth entry
ax.legend(handles2[::5], labels2[::5], title='Elevation [m]')