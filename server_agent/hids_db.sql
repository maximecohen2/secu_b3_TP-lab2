CREATE TABLE Role (
  role_id INTEGER NOT NULL,
  role_label VARCHAR(80) NOT NULL,
	CONSTRAINT PK_role PRIMARY KEY (role_id)
);

CREATE TABLE Status (
  stat_id INTEGER NOT NULL,
  stat_label VARCHAR(80) NOT NULL,
	CONSTRAINT PK_stat PRIMARY KEY (stat_id)
);

CREATE TABLE Site (
  site_id INTEGER NOT NULL,
  site_name VARCHAR(70) NOT NULL,
  site_address VARCHAR(80) NOT NULL,
  site_date DATE NOT NULL,
  site_ssh_connection BOOLEAN NOT NULL,
  site_fileignore_name VARCHAR(50) NOT NULL,
  site_fileignore_path VARCHAR(255) NOT NULL,
	CONSTRAINT PK_site PRIMARY KEY (site_id)
);

CREATE TABLE User (
  user_id INTEGER NOT NULL,
  user_role_id INTEGER NOT NULL,
  user_date DATE NOT NULL,
  user_mail VARCHAR(70) NOT NULL,
  user_login VARCHAR(30) NOT NULL,
  user_password VARCHAR(255) NOT NULL,
	CONSTRAINT PK_user PRIMARY KEY (user_id),
	CONSTRAINT FK_user_role FOREIGN KEY (user_role_id) REFERENCES Role(role_id)
);

CREATE TABLE Hash (
  hash_id INTEGER NOT NULL,
  hash_date DATE NOT NULL,
  hash_site_id INTEGER NOT NULL,
  hash_status_id INTEGER NOT NULL,
  hash_file_name VARCHAR(70) NOT NULL,
  hash_file_path VARCHAR(255) NOT NULL
	CONSTRAINT PK_hash PRIMARY KEY (hash_id),
	CONSTRAINT FK_hash_site FOREIGN KEY (hash_site_id) REFERENCES Site(site_id),
	CONSTRAINT FK_hash_status FOREIGN KEY (hash_status_id) REFERENCES Status(status_id)
);

CREATE TABLE UserSite (
  us_id INTEGER NOT NULL,
  us_user_id INTEGER NOT NULL,
  us_site_id INTEGER NOT NULL
	CONSTRAINT PK_us PRIMARY KEY (us_id),
	CONSTRAINT FK_us_user FOREIGN KEY (us_user_id) REFERENCES User(user_id),
	CONSTRAINT FK_us_site FOREIGN KEY (us_site_id) REFERENCES Site(site_id)
);
