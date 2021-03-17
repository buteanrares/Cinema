# Cinema
 ## Application implemented with Python using OOP and Stratified Architecture. Designed for cinema management, supporting movies, clientcards and reservations.
 
 ### Cinema application with the following functionalities:
- [x] CRUD operations  for:
  - Movie
     - ID, title, release year, ticket price, in schedule
  - Clientcard
      - ID, surname, forename, SSN, birthdate, registration date, points
  - Reservation
      - ID, movie ID, clientcard ID, date, time
- [x] Saving and reading locally with serialization into .pickle files
- [x] Listing implemented for all domain objects, with extended functionalities:
    - Listing reservations by datetime interval
    - Listing most popular movies based on reservations number
    - Listing most points-rich clients
- [x] Removal of all movies inside a datetime interval
- [x] Custom bonus points gifting to clients whose birthdate is equal to a given day 
- [x] Text-based binary search implemented for all domain objects 
- [x] Populate domain objects with custom amount
- [x] Optimized undo & redo operations using lambda functions
- [x] Broad UnitTesting 
- [x] Domain-level objects validation

> NOTES: 
> * Clientcard SSN is unique
> * Clients accumulate 10% of movie price as bonus points

