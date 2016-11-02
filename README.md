Here's my solution for the technical test at EMBL-EBI.  

The code is far from perfect and can be optimized better (especially the structure for storing matrix needs an improvement!).  

Quite a bit of time has been spent for formatting output matrix in a nice way.  

The output looks in a following way (though, marking is not the same, so better to run from the terminal):  



|                | Public, J Q    | Doe, John      | Doe, Jane      | Smith, John    
----------------------------------------------------------------
| Public, J Q    | 0              | 1              | 1              | 0              
| Doe, John      | 1              | 0              | 1              | 1              
| Doe, Jane      | 1              | 1              | 0              | 0              
| Smith, John    | 0              | 1              | 0              | 0              

