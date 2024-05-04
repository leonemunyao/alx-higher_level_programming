-- A Script that converts htb_0c_0 to UTF8(utf8mb4, collate utfmb4_unicode_ci). The following are to be converted to UTF8; Database htbn_0c_0, Table first_table, Field name in first_table.

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
