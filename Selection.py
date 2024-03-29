selection_start = ['from', 'import', 'if', 'for', 'while', 'try', 'pass', 'id', 'continue', 'break', 'return', 'public', 'private', '$']
selection_import_st = ['from', 'import']
selection_from_st = ['from', 'import']
selection_from_id = ['id']
selection_from_id_prime = ['.', 'import']
selection_im_id = ['id']
selection_im_id_prime = ['.', 'as', '$']
selection_as_st = ['as', '$']
selection_sst = ['if', 'for', 'while', 'try', 'pass', 'id', 'continue', 'break', 'return', 'def', '}']
selection_if_else = ['if']
selection_if_body = ['{']
selection_mst = ['if', 'for', 'while', 'try', 'pass', 'id', 'continue', 'break', 'return', 'def', '}']
selection_else = ['else', 'if', 'for', 'while', 'try', 'pass', 'id', 'continue', 'break', 'return', 'def', '{', '}', 'except', '$']
selection_body = ['{']
selection_loops = ['for', 'while']
selection_for_st = ['for']
selection_while_st = ['while']
selection_loop_prime = ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']
selection_exp = ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']
selection_or_exp = ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']
selection_or_exp_prime = ['or', '}']
selection_and_exp = ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']
selection_and_exp_prime = ['and', 'or', '}']
selection_in_exp = ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']
selection_in_exp_prime = ['MO', 'and', 'or', '}']
selection_is_exp = ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']
selection_is_exp_prime = ['IO', 'MO', 'and', 'or', '}']
selection_ro_exp = ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']
selection_ro_exp_prime = ['PM', 'RO', 'IO', 'MO', 'and', 'or', '}']
selection_pm_exp = ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']
selection_pm_exp_prime = ['PM', 'RO', 'IO', 'MO', 'and', 'or', '}']
selection_dm_exp_prime = ['DM', '*', 'PM', 'RO', 'IO', 'MO', 'and', 'or', '}']
selection_dm_exp = ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']
selection_power_exp = ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not', '*']
selection_end_exp = ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']
selection_const = ['int_const', 'float_const', 'string_const', 'char_const', 'bool_const']
selection_fn_def = ['public', 'private', 'if', 'for', 'while', 'try', 'pass', 'id', 'continue', 'break', 'return', 'def', '{', '}']
selection_fn_def_prime = ['int', 'str', 'float', 'char', ')']
selection_fn_def_doubleprime = [',', ')']
selection_ret_type = ['int', 'str', 'char', 'float', 'none', 'list', 'dict', 'id']
selection_type = ['int', 'str', 'char', 'float', 'none', 'list', 'dict', 'id']
selection_type_prime = ['list', 'dict']
selection_type_doubleprime = ['id', 'dict', 'list', 'none', 'float', 'char', 'str', 'int']
selection_mul_type = [',', ']']
selection_dt = ['int', 'str', 'char', 'float']
selection_ret = ['return', 'if', 'for', 'while', 'try', 'pass', 'id', 'continue', 'break', 'return', 'def', '}']
selection_ret_prime = ['(', 'id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', 'not']
selection_try_st = ['try']
selection_except = ['except']
selection_except_doubleprime = ['except', 'else', 'finally', '$']
selection_except_prime = ['id']
selection_as = ['as', '{']
selection_finally = ['finally', '$']
selection_else_doubleprime = ['else']
selection_ss = ['self', 'super', 'id']
selection_class_def = ['public', 'private', '$']
selection_class_type = ['abstract', 'static', 'sealed', 'def']
selection_cid = ['(', '{']
selection_mul_id = [',']
selection_csst = ['if', 'for', 'while', 'try', 'pass', 'self', 'super', 'public', 'private', 'abstract', 'static', 'sealed', 'def', 'return', 'break', 'continue', 'int', 'str', 'char', 'float', 'def', 'id', '}']
selection_c_body = ['{']
selection_c_mst = ['if', 'for', 'while', 'try', 'pass', 'self', 'super', 'public', 'private', 'abstract', 'static', 'sealed', 'def', 'return', 'break', 'continue', 'int', 'str', 'char', 'float', 'def', '}']
selection_access_modifier = ['public private', 'id', '{', 'class_id']
selection_assign_st = ['id']
selection_a2 = ['.', '[', '(', 'AO', '=']
selection_a3 = ['.', '[', 'AO', '=']
selection_mul_arr = [',']
selection_mul_dict = [',', '}']
selection_dict = []
selection_arr = ['[', '{not', '(', 'id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', ']']
selection_assign = ['AO', '=']
selection_arr_dict = ['[', '{']
selection_ref = ['id']
selection_ref_prime = ['.', '[', '(', ';']
selection_ref_doubleprime = ['.', ';']
selection_para = ['not', '(', 'id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', ']']
selection_mul_pa = [',', 'int_const', 'bool_const', 'char_const', 'string_const', 'float_const', 'string_const', '(', 'not', ']']
selection_dec_doubleprime = [';', ',']
selection_init = ['id', '=', 'if', 'for', 'while', 'try', 'pass', 'id', 'continue', 'break', 'return', 'def', '}', ';', ',']
selection_init_prime = ['[', '{', ';']
selection_ld_dec = ['[', '{}']
selection_dec_prime = ['{', '[', 'id', '=', 'if', 'for', 'while', 'try', 'pass', 'continue', 'break', 'return', 'def', '}']
selection_dec = ['int', 'str', 'float', 'char']
