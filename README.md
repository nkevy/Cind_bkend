Cind_bkend
=============
Author: Noah Kevy

Description:
------------
A back end for the Cind App. The Api is written in python to allow verified Cind Clients access to data. The Cind database is a postgresql system. 

Dependencies:
-------------
Postgress sql database
	database: mind
		tabels: words:
				lect (char 40, not null) 
				clock (timestamp without time zone, not null)
				new (boolean, not null)
				old (boolean, not null)
			 memory:
				src (char 40, not null)
				dst (char 40, not null)
				dyad numeric(5,2)
