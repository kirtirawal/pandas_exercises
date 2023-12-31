#!/usr/bin/en
# -*- coding: utf-8 -*-

"""
    This file is part of aialchemyhub_in
    (https://github.com/satya25/aialchemyhub_in).

    aialchemyhub_in is free software repository:seaborn
    You can redistribute it and/or modify it under
    the terms of the MIT License.

    aialchemyhub_in is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    MIT License for more details.

    You should have received a copy of the MIT License along with
    aialchemyhub_in.  If not, see <https://opensource.org/licenses/MIT>.
"""

# ----------------------------------------------------------------------------
# File Name         :       example_1.py
# Created By        :       
# Created Date      :       Dec 30, 2023
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       numpy
#
# Installation      :       $ pip install --upgrade numpy flake8 autopep8 black pylint mypy pytest
#
# Usage             :       python ./seaborn/example_1.py
#
# ---------------------------------------------------------------------------
#
# Credits and Acknowledgements
#
# - Special thanks to the seaborny community for their excellent library:
#   https://seaborn.pydata.org/
#
# - The APIs used in this script is documented here:
#  https://seaborn.pydata.org/api.html
#
# - Code Snippet(s) adapted from    :   -- NOT Applicable --
#
# - Dataset(s) sourced  from        :   -- NOT Applicable --
#
#
# - Inspiration for Seaborn drawn from:
#   https://seaborn.pydata.org/tutorial/introduction.html
#
# Thank you to the creators and maintainers of these resources!
#
# ---------------------------------------------------------------------------
#
# - Content Removal Requests
#
#   If you are the owner or creator of any content used in this script and
#   would like it to be removed, please contact me at:  spnigam25@yahoo.com
#   I will promptly remove the content upon request.
#
# ---------------------------------------------------------------------------

# Importing intrinsic libraries:
import logging
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    # Configure logging
    # creating log file name from current script name

    log_file_name = os.path.splitext(__file__)[0]
    logging.basicConfig(
        filename=log_file_name,
        level=logging.INFO,
        format= "%(asctime)s - %(levelname)s - %(message)s",
    )

    try :
        file_name = os.path.basename(__file__)
        logging.info("%s : Library Installaton and Setup Complete. You can load the Dataset.", file_name)
        print("Library Installaton and Setup Complete. You can load the Dataset")

        #Load the Dataset
        # Load an example dataset
        fifa_data = sns.load_dataset("fifa")
        print(fifa_data.columns)
        
        # Set the width and height of the figure
        plt.figure(figsize=(16,6))

        # Line chart showing how FIFA rankings evolved over time                 
        print(sns.lineplot(data=fifa_data))
        
        except (ValueError, TypeError) as e:
        logging.error("An error occurred: %s", e)
        print(
            "An unexpected error occurred. \
            Please check the logs for details."
        )
if __name__ == '__main__':
    main()




















