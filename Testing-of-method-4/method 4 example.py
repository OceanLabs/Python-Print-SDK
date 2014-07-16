default_settings = {
  'setting_a' : "foo",
'setting_b' : "bar",
'setting_c' : "spam",
'setting_d' : "jam"
}# example set-up for the default parameters

dynamic_settings = default_settings # default parameters are turned into editable parameters

def edit_settings(dynamic_settings): # a modual for editing the settings of the order,
                                     # very simple at the moment but has possibility for a propper interface
  accept_settings = ['setting_a', 'setting_b', 'setting_c', 'setting_d']
  print("Input setting you wish to change or 0 if you are finished.")
  changing_setting = input()
  if changing_setting in accepted_settings:
    print("Please input new value for " + changing_setting)
    new_value = input()
    dynamic_setting[changing_setting] = new_value
  return dynamic_setting

editting = True # don't mind this, it's just for the loop bellow, for loop can be used if it is neater

while editting: # loop for editing settings, yes I know it may be tedious to edit each setting one by one but it works!
  dynamic_settings = edit_settings(dynamic_settings)
  keep_editing = input("Do you wish to continue editing? (y/n)\n")
  if keep_editing == 'n':
    editting = False
