#Q1
#use database
USE world;

#1.1
#find the amount of records that have indepyear in 20th century
SELECT count(*)  FROM country WHERE IndepYear > 1901 AND IndepYear <= 2000;

#1.2
#calculate the sum of "Population" of the countries that have expected life of 75 years
SELECT sum(Population) FROM country WHERE LifeExpectancy >= 75;

#1.3
#obtain world population = 6078749450
SELECT sum(Population) FROM country;

#obtain top 10 countries with highest population as percentage of the world population
SELECT Name,Population/6078749450 FROM country ORDER BY population DESC LIMIT 0,10;

#1.4
#sort all countries by population density descendingly and pick top 10. ***Macao and Hongkong are not countries though***
SELECT Name,Population/SurfaceArea FROM country ORDER BY Population/SurfaceArea DESC LIMIT 0,10;

#1.5
#obtain all countries grouped by Region, sorted descendingly
SELECT Region,count(Name) AS country_count FROM country GROUP BY Region ORDER BY country_count DESC;

#1.6
#obtain and sort CountryCode under condition of language count > 10 in descending order
SELECT CountryCode, count(Language) AS language_count FROM countrylanguage GROUP BY CountryCode HAVING language_count > 10 ORDER BY language_count DESC;
   
