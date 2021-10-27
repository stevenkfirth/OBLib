.. OBLib documentation master file, created by
   sphinx-quickstart on Wed Oct 27 10:13:45 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to OBLib's documentation!
=================================

OBLib is a Python package of occupant behaviour models for IEA EBC Annex 79.

The package contains a series of models for predicitng the behaviour of occupants in buildings. 
The models are either deterministic or stotastic and include modelling techniques such as scheduling, markov chain and logistic regression.

It is anticipated that the outputs of the behaviour models will be of use in specifying occupant behaviour in building simulation tools.

.. toctree::
   :maxdepth: 2
   :caption: Start here:
   
   Introduction

.. toctree::
   :maxdepth: 2
   :caption: General models:

   ScheduleModel

.. toctree::
   :maxdepth: 2
   :caption: Thermostat models:
   
   SAP2012ThermostatModel


.. toctree::
   :maxdepth: 2
   :caption: Abstract models:

   Model
   DeterministicModel
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
