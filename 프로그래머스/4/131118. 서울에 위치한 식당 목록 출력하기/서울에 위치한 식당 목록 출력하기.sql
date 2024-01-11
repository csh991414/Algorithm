SELECT R.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE), 2) SCORE
FROM REST_REVIEW R, REST_INFO I
WHERE I.ADDRESS LIKE '서울%'
AND R.REST_ID=I.REST_ID
GROUP BY R.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC;