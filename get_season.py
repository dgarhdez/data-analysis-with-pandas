{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from datetime import date\n",
    "\n",
    "def get_season(date_to_convert: datetime.date):  # the function expects a datetime.date object as input\n",
    "    \n",
    "    # fix the year of the input\n",
    "    date_year = date_to_convert.year\n",
    "    \n",
    "    # create the list of tuples on which to loop\n",
    "    seasons = [\n",
    "        (\"winter\", date(date_year, 12, 21), date(date_year, 12, 31)),\n",
    "        (\"spring\", date(date_year, 3, 20), date(date_year, 6, 21)),\n",
    "        (\"summer\", date(date_year, 6, 22), date(date_year, 9, 21)),\n",
    "        (\"fall\", date(date_year, 9, 22), date(date_year, 12, 20)),\n",
    "        (\"winter\", date(date_year, 1, 1), date(date_year, 3, 19))\n",
    "    ]\n",
    "    \n",
    "    # loop for each season trying to find the season to which\n",
    "    # date_to_convert belongs to\n",
    "    for elem in seasons:  # season = tuple(name, start, end) = (elem[0], elem[1], elem[2])\n",
    "        if date_to_convert>=elem[1] and date_to_convert<=elem[2]:  \n",
    "            return elem[0]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (mbd)",
   "language": "python",
   "name": "mbd"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.0"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
