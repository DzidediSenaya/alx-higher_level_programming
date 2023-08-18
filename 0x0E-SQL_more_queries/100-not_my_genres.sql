-- Get the genre name(s) of the show Dexter
SELECT DISTINCT `g`.`name`
FROM `tv_genres` AS `g`
INNER JOIN `tv_show_genres` AS `s`
ON `g`.`id` = `s`.`genre_id`
INNER JOIN `tv_shows` AS `t`
ON `s`.`show_id` = `t`.`id`
WHERE `g`.`name` NOT IN (
  SELECT `g2`.`name`
  FROM `tv_genres` AS `g2`
  INNER JOIN `tv_show_genres` AS `s2`
  ON `g2`.`id` = `s2`.`genre_id`
  INNER JOIN `tv_shows` AS `t2`
  ON `s2`.`show_id` = `t2`.`id`
  WHERE `t2`.`title` = "Dexter"
)
ORDER BY `g`.`name`;
