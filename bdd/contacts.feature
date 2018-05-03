Scenario Outline: Add new contact
  Given A contact list
  Given A contact with <first_name>, <last_name>, <home_phone>, <work_phone>, <mobile_phone>, <secondary_phone>, <email_1>, <email_2>, <email_3>, <address>
  When I add the contact to the list
  Then New contact list is equal to the old list with the added contact

  Examples:
  | first_name | last_name | address | home_phone| work_phone| mobile_phone| secondary_phone| email_1| email_2| email_3|
  | name1      | last_name1| address1| 9214410883| 9214410883| 9214410883  | 9214410883     | asasd  | adasda | adasdas|
  | name2      | last_name2| address2| 9214410883| 9214410883| 9214410883  | 9214410883     | asasd  | adasda | adasdas|


Scenario: Delete a contact
  Given A non-empty contact list
  Given A random contact from the list
  When I delete the contact from the list
  Then The new list is equal to the old list without the deleted contact


Scenario: Edit a contact
  Given A non-empty contact list
  Given A random index
  Given A random contact from the list
  Given A contact to edit
  When I edit the contact from the list
  Then The new list is equal to the old list with edited contact