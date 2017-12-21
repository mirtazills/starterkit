.. _managing_observations:

=====================
Managing observations
=====================

An **observation** is an action whose result is an estimate of the value of some property of the feature-of-interest (i.e. station, animals or tissue), at a specific point in time, obtained using a specified procedure or sensor (After Cox 2008 cited by
INSPIRE Cross Thematic Working Group on Observations & Measurements, 2011). For that reason, every observation need to be associated with a specific, well-described sensor which have collected the data.

In this section, you will learn how to share sensors observations through specific web services (Sensor Observation Services, `SOS <http://www.opengeospatial.org/standards/sos>`_) to manage observations by following a two-steps pipeline: 

   
#. describe sensor by creating sensors metadata (**Register a new sensor**)
#. upload sensor observations by associating them to registered sensors (**Upload observations**)

You can access to both these functions through the GET-IT home page by clicking Sensors. 

.. figure:: GETIT_Sensor_Interface.png
   :align: center

By clicking **Explore SOS** you can access to the sensors registered in the local repository and to **Register a new sensors** section. More information in :ref:`sensors_metadata`

By clicking **Upload observations** you can upload observations by selecting the associated sensor. More information in :ref:`upload_observations`


All the functionality making SWE pure requests.

.. toctree::
   :maxdepth: 4

   sensors_metadata
   metadata_check
   upload_observations
