**Overview**  
Down below you can find information on how to properly import and run the file I created.
I wanted to mention ChatGPT was used for code that imported the database over to my query.
The import wizard import method mentioned on the slide would have taken hours if not days
to fully import the database. 


**Before you get started…**

**What you'll Need:**

* MySQL installed  
* Verify that MySQL Workbench connection is properly set up  
* Download the database SFPL\_DataSF\_library-usage\_Jan\_2023.csv

If you don’t have MySQL install please refer to this link for installation:  
[https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/)

Alternatively (and preferably) refer to A360 presentation 13, starting on slide 44 

To get the database .csv please refer to the link below for download:  
[https://github.com/KathiraveluLab/SFILS/](https://github.com/KathiraveluLab/SFILS/)

**Getting Started:**

Upload the SFPL\_DataSF\_library-usage\_Jan\_2023.csv to MySQL  
   a. Enable hidden items in you file explorer

   b. Navigate to *ProgramData* and paste the file in the *Upload* folder.

   c. Navigate back to the MySQL 8.0 open *my.ini* using notepad

   d. Below *\[mysqld\]*  enter in *local-infile=1*, save the changes and close out Notepad.

   **Note:** If you receive a permission error, create a new *my.ini* via Notepad running as an admin. Copy and paste the content of the original *my.ini* to the new one with the changes made to *\[mysqld\]*. Delete the original *my.ini* and rename the new file to *my.ini* to take its place.


   e. Open *MySQL* *Workbench* application

   f. Create a new *MySQL* connection if one isn’t already created.

   g. Click on the *wrench,* the name of the connection, advanced, and then add *OPT\_LOCAL\_INFILE=1* to the box labeled    others. Close out the box afterwards.

   h. Directly click on your project’s connection to open up the project. Copy paste my script to the *red *highlighted* tab below. Then run it by selecting the *lightning* icon.

