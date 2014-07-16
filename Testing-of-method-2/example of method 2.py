edited_parameters = {
'setting_a' : '',
'setting_b' : '',
'setting_c' : '',
'setting_d' : ''
}

default_parameters = default_example_parameters()

def example_ordering_module(edited_parameters):
  from method_2_test_defaults import default_example_parameters
  default_parameters = default_example_parameters()
  
  Ledited_parameters = [
  edited_parameters['setting_a'],
  edited_parameters['setting_b'],
  edited_parameters['setting_c'],
  edited_parameters['setting_d']
  ]
  
  Ldefault_parameters = [
  default_parameters['setting_a'],
  default_parameters['setting_b'],
  default_parameters['setting_c'],
  default_parameters['setting_d'],
  ]
  
  for i in range(0, len(Ledited_parameters)):
    if Ledited_parameter[i] != '':
      Ldefault_parameter[i] = Ledited_parameter[i]
  
  default_parameters['setting_a'] = Ldefault_parameter[0]
  default_parameters['setting_b'] = Ldefault_parameter[1]
  default_parameters['setting_c'] = Ldefault_parameter[2]
  default_parameters['setting_d'] = Ldefault_parameter[3]
  
  place_order_parameters(default_parameters)
