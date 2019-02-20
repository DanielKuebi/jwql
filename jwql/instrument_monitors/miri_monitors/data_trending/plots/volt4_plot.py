import jwql.instrument_monitors.miri_monitors.data_trending.utils.sql_interface as sql
import jwql.instrument_monitors.miri_monitors.data_trending.plots.plot_functions as pf
from bokeh.plotting import figure, output_file, show
from bokeh.models import BoxAnnotation
from bokeh.embed import components

import numpy as np

from astropy.time import Time

def volt4(conn):

    #query data from database
    columns = ('start_time, average, deviation')
    volt4_idle = sql.query_data(conn, 'IMIR_HK_ICE_SEC_VOLT4_IDLE', columns)
    volt4_hv = sql.query_data(conn, 'IMIR_HK_ICE_SEC_VOLT4_HV_ON', columns)

    #append data from query to numpy arrays
    volt4_idle_time, volt4_idle_val, volt4_idle_dev = pf.split_data(volt4_idle)
    volt4_hv_time, volt4_hv_val, volt4_hv_dev = pf.split_data(volt4_hv)

    #prepare ploynom regression
    volt4_hv_reg = pf.pol_regression(volt4_hv_time, volt4_hv_val, 3)
    volt4_idle_reg = pf.pol_regression(volt4_idle_time, volt4_idle_val, 3)

    idle_time = Time(volt4_idle_time, format = "mjd").datetime
    hv_time = Time(volt4_hv_time, format = "mjd").datetime

    # create a new plot with a title and axis labels
    p = figure( tools = "pan,wheel_zoom,box_zoom,reset,save",       \
                toolbar_location = "above",                         \
                plot_width = 560,                                   \
                plot_height = 500,                                  \
                y_range = [4.2,5],                                  \
                x_axis_type = 'datetime',                           \
                x_axis_label = 'Date', y_axis_label='Voltage (V)')

    p.grid.visible = True

    # configure visual properties on a plotś title attribute
    p.title.text="ICE_SEC_VOLT4"
    p.title.align = "left"
    p.title.text_color = "#c85108"
    p.title.text_font_size = "25px"

    p.background_fill_color = "#efefef"
    #p.xgrid.grid_line_color = '#efefef'

    # add a line renderer with legend and line thickness
    p.scatter(idle_time, volt4_idle_val, color = 'red', legend = "Volt4 idle")
    p.scatter(hv_time, volt4_hv_val, color = 'orange', legend = "Volt4 HV on ")

    p.line(hv_time, volt4_hv_reg , color = 'green', legend = "Idle regression")
    p.line(idle_time, volt4_idle_reg, color = 'blue', legend = "HV regression")

    p.legend.location = "bottom_right"
    p.legend.click_policy = "hide"

    return p