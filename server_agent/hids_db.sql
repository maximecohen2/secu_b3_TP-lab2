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

CREATE TABLE Person (
  pers_id INTEGER NOT NULL,
  pers_role_id INTEGER NOT NULL,
  pers_date DATE NOT NULL,
  pers_mail VARCHAR(70) NOT NULL,
  pers_login VARCHAR(30) NOT NULL,
  pers_password VARCHAR(255) NOT NULL,
	CONSTRAINT PK_pers PRIMARY KEY (pers_id),
	CONSTRAINT FK_pers_role FOREIGN KEY (pers_role_id) REFERENCES Role(role_id)
);

CREATE TABLE Hash (
  hash_id INTEGER NOT NULL,
  hash_date DATE NOT NULL,
  hash_site_id INTEGER NOT NULL,
  hash_status_id INTEGER NOT NULL,
  hash_file_name VARCHAR(70) NOT NULL,
  hash_file_path VARCHAR(255) NOT NULL,
	CONSTRAINT PK_hash PRIMARY KEY (hash_id),
	CONSTRAINT FK_hash_site FOREIGN KEY (hash_site_id) REFERENCES Site(site_id),
	CONSTRAINT FK_hash_status FOREIGN KEY (hash_status_id) REFERENCES Status(status_id)
);

CREATE TABLE PersonSite (
  ps_id INTEGER NOT NULL,
  ps_pers_id INTEGER NOT NULL,
  ps_site_id INTEGER NOT NULL,
	CONSTRAINT PK_ps PRIMARY KEY (ps_id),
	CONSTRAINT FK_ps_pers FOREIGN KEY (ps_pers_id) REFERENCES Person(pers_id),
	CONSTRAINT FK_ps_site FOREIGN KEY (ps_site_id) REFERENCES Site(site_id)
);
