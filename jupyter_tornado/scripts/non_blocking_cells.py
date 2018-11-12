""" Non-blocking Jupyter Cell Execution.

Example of using Tornado's asynchronous loop to be able to run cells
asynchronously in a notebook with a cell magic.

References
----------
https://www.tornadoweb.org/en/stable/ioloop.html
 """
from IPython import get_ipython
from IPython.core.magic import register_cell_magic
from tornado import ioloop
from functools import partial


def cell_done_callback(*args, **kwargs):
    """ Do things after the cell executes """
    pass


@register_cell_magic
def non_blocking_cell(line, cell):
    async_loop = ioloop.IOLoop.instance()
    ipy = get_ipython()
    executor = None
    future = async_loop.run_in_executor(executor, partial(ipy.run_cell, raw_cell=cell))
    #  Placeholder to add functionalilty like alerts after cell completes.
    future.add_done_callback(cell_done_callback)
