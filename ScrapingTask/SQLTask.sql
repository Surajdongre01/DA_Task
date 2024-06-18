CREATE TABLE sp500_companies (
    Symbol varchar(20),
    Security varchar(255),
    GICS_Sector varchar(255),
    GICS_Sub_Industry varchar(255),
    Headquarters_Location varchar(255),
    Date_added DATE,
    CIK varchar(30),
    Founded varchar(50)
);

select * from sp500_companies

COPY sp500_companies
FROM 'D:/Internship/Python/JS/sp500_companies.csv'
DELIMITER ','
CSV HEADER;

select * from sp500_companies  

UPDATE sp500_companies
SET Founded = TRIM(SUBSTRING(Founded FROM '^[^()]+'))
WHERE POSITION('(' IN Founded) > 0;

UPDATE sp500_companies
SET Founded = TRIM(SPLIT_PART(Founded, '/', 1));

select * from sp500_companies


CREATE TABLE Sectors (
    SectorID serial PRIMARY KEY ,
    SectorName varchar(100) NOT NULL
);

select * from sectors

INSERT INTO Sectors (SectorName)
SELECT DISTINCT GICS_Sector
FROM sp500_companies;




CREATE TABLE Industries (
    IndustryID serial PRIMARY KEY ,
    IndustryName varchar(100) NOT NULL,
    SectorID INT,
    FOREIGN KEY (SectorID) REFERENCES Sectors(SectorID)
);

select * from industries  

INSERT INTO Industries (IndustryName, SectorID)
SELECT DISTINCT 
    s.GICS_Sub_Industry,
    se.SectorID
FROM sp500_companies as s
JOIN Sectors as se ON s.GICS_Sector = se.SectorName;




CREATE TABLE Headquarters (
    HeadquartersID serial PRIMARY KEY ,
    Location varchar(255) NOT NULL
);

select * from Headquarters  

INSERT INTO Headquarters (Location)
SELECT DISTINCT Headquarters_Location
FROM sp500_companies;




CREATE TABLE Companies (
    CompanyID serial PRIMARY KEY ,
    CompanyName varchar(255) NOT NULL,
    TickerSymbol varchar(10) NOT NULL,
    IndustryID int,
    HeadquartersID int,
    DateAdded date,
    CIK varchar(10),
    Founded varchar(10),
    FOREIGN KEY (IndustryID) REFERENCES Industries(IndustryID),
    FOREIGN KEY (HeadquartersID) REFERENCES Headquarters(HeadquartersID)
);

select * from companies


INSERT INTO Companies (CompanyName, TickerSymbol, IndustryID, HeadquartersID, DateAdded, CIK, Founded)
SELECT 
    s.Security,
    s.Symbol,
    i.IndustryID,
    h.HeadquartersID,
    s.Date_added,
    s.CIK,
    s.Founded
FROM sp500_companies s
JOIN Industries i ON s.GICS_Sub_Industry = i.IndustryName
JOIN Headquarters h ON s.Headquarters_Location = h.Location;

