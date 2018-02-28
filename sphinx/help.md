### A note on Help with Shyft
Shyft is designed to make use of standard help functionality in Python. You are able to access help functionality using tab completion or `help()`. The "?" or "??" standards in IPython work, but seem at times to be limited with respect to some of the `Boost-Python` documentation. Therefore, we encourage you to please use `help`.


#### Is the help text unfamiliar?
Look at the following examples. Note that in some cases, the doc strings are generated directly from the C++ underlying code, so you will see full C++ call signatures. If you use `help(shyft_object)` and get something that is looks a bit overwhelming or unfamiliar, just realize that the methods are generally showing how to call a method and what it returns. If you see `(object)arg1` or `(object)self` as a first argument to a method, that simply means `the class itself is the first argument <https://www.programiz.com/article/python-self-why>`_.

If you are not familiar with C++ one aspect to be aware of is [Overloading](https://www.tutorialspoint.com/cplusplus/cpp_overloading.htm). Due to this, when you print `help()` for a `shyft.api` function you may see multiple `_init_` definitions (e.g. call structures). You'll have to use logic to reason which is applicable to your case.

See for example:

    help(region_model.set_state_collection)

Returns:

    Help on method set_state_collection:

    set_state_collection(...) method of  shyft.api.pt_gs_k._pt_gs_k.PTGSKModel instance
    set_state_collection( (PTGSKModel)arg1, (int)catchment_id, (bool)on_or_off) -> None :
        enable state collection for specified or all
        cells note that this only works if the underlying
        cell is configured to do state collection. This
        is typically not the  case for cell-types that
        are used during calibration/optimization

What this means is that *method* `set_state_collection` has a call signature as: `set_state_collection( (PTGSKModel)arg1, (int)catchment_id, (bool)on_or_off) -> None`
This means, the method should be called with the first positional argument as the model, or `self`, so **this is already there** when you call it from `region_model`. The second positional argument should be an integer referring to the catchment_id (more on this later), and the third is a boolean indicating True or False. So to make use of this *method* you would call it like:

    simulator.region_model.set_state_collection(1228, False)

And state collection would be turned *off* for catchment with `catchment_id == 1228`.

Another example coming from the api:

See for example:

    help(shyft.api.Calendar)

Will have in the docstring:

    Methods defined here:

    __init__(...)
        __init__( (object)arg1) -> None

        __init__( (object)arg1, (int)tz_offset) -> None :
            creates a calendar with constant tz-offset

            Parameters
            ----------
            tz_offset : int
                seconds utc offset, 3600 gives UTC+01 zone


        __init__( (object)arg1, (str)olson_tz_id) -> None :
            create a Calendar from Olson timezone id, eg. 'Europe/Oslo'

            Parameters
            ----------
            olson_tz_id : str
                Olson time-zone id, e.g. 'Europe/Oslo'

What this means is that the *Class* `Calendar` may be instantiated as: `Calendar()` returning an empty Calendar, as `Calendar( tz_offset )` where `tz_offset` is a integer indicating the offset from the timezone, or as `Calendar( 'Europe/Oslo')` where the calendar will be 'tied' to the "Europe/Oslo" timezone (otherwise UTC).

Okay, so now you are ready to explore Shyft internals further! Remember, *use `help()`*!!