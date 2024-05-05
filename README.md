# DBMS_PROJECT
LIBRARY_MANAGEMNET_SYSTEM
**Library Management System Database Setup Guide**

Overview:
This guide provides instructions for setting up the database schema and triggers for a Library Management System (LMS). The database schema is designed to efficiently manage various aspects of library operations, including book management, borrower registration, book issuance, and more. Triggers are implemented to enforce business rules and maintain data consistency.

1 Insert Data: Populate the tables with sample data using `INSERT INTO` statements.

2. Create Triggers:
   - `before_insert_pending_book_requests`: Ensures that pending book requests are processed only if the requesting member has a sufficient balance.
   - `book_issued_trigger_function`: Automatically updates the number of available copies of a book in the library after issuance.

3. Create Indexes:Execute the SQL commands to create indexes for optimized querying on the following columns:
   - `isbn` in the `book` table
   - `username` in the `member` table
   - `title` in the `book` table
   - `PublisherName` in the `table_book` table
   - `member` in the `pending_book_requests` table

4.Searching Books:
Execute SQL queries to search for books based on title, author, category, or ISBN.

5.Updating Book Information:
Update book information using SQL `UPDATE` statements, specifying the ISBN of the book to be updated.

Conclusion:
The database schema and triggers provide a robust foundation for the Library Management System, facilitating efficient data management, integrity, and security. With proper indexing and triggers, the system is equipped to handle the demands of a modern library environment while ensuring optimal performance and functionality.


