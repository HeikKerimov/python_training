Scenario Outline: Add new group
  Given A group list
  Given A group with <name>, <header> and <footer>
  When I add the group to the list
  Then New group list is equal to the old list with the added group

  Examples:
  | name | header | footer |
  | name1| header1| footer1|
  | name2| header2| footer2|


Scenario: Delete a group
  Given A non-empty group list
  Given A random group from the list
  When I delete the group from the list
  Then The new list is equal to the old list without the deleted group