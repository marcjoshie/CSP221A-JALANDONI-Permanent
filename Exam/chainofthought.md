since there are datas Lists & TuplesBoth are ordered sequences. Lists are mutable, meaning you can change them after creation. Tuples are immutable — fixed once built. Use tuples for fixed records (like coordinates); use lists for collections that grow or shrink.

My understanding of the task here is the system evaluates and validates the scores on construction per rule and inlcluding locks as resources need to be reliably cleaned up whether or not an error occurs. The InvalidScoreError and StudentRecordLockedError exception handlers catches the  information for the caller to understand what happened, raised wherever rules 1 and 2 required them to do. This is also why the order of except clauses matters: catch more specific exceptions before more general ones. 

Making Objects Debuggable — __str__ and __repr__  on Student per rule 3. Using Lamda and Numpy Cleaning a fine-tuning dataset the scores of the students 

Last printing Deduplicating a fine-tuning datas of the score of the student will use vectorization