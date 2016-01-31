
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '1B8F68937D9DB871BCA4DE6FC1FB9FEF'
    
_lr_action_items = {'TkSuma':([1,2,3,4,11,12,13,14,15,16,17,],[-7,6,-6,-8,6,-1,-2,-3,-4,-5,-9,]),'TkResta':([1,2,3,4,11,12,13,14,15,16,17,],[-7,7,-6,-8,7,-1,-2,-3,-4,-5,-9,]),'TkMult':([1,3,4,12,13,14,15,16,17,],[-7,8,-8,8,8,-3,-4,-5,-9,]),'TkMod':([1,3,4,12,13,14,15,16,17,],[-7,10,-8,10,10,-3,-4,-5,-9,]),'$end':([1,2,3,4,12,13,14,15,16,17,],[-7,0,-6,-8,-1,-2,-3,-4,-5,-9,]),'TkNum':([0,5,6,7,8,9,10,],[4,4,4,4,4,4,4,]),'TkDiv':([1,3,4,12,13,14,15,16,17,],[-7,9,-8,9,9,-3,-4,-5,-9,]),'TkParAbre':([0,5,6,7,8,9,10,],[5,5,5,5,5,5,5,]),'TkParCierra':([1,3,4,11,12,13,14,15,16,17,],[-7,-6,-8,17,-1,-2,-3,-4,-5,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,5,6,7,],[3,3,12,13,]),'factor':([0,5,6,7,8,9,10,],[1,1,1,1,14,15,16,]),'expression':([0,5,],[2,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression TkSuma term','expression',3,'p_binary_operators','SinBot.py',24),
  ('expression -> expression TkResta term','expression',3,'p_binary_operators','SinBot.py',25),
  ('term -> term TkMult factor','term',3,'p_binary_operators','SinBot.py',26),
  ('term -> term TkDiv factor','term',3,'p_binary_operators','SinBot.py',27),
  ('term -> term TkMod factor','term',3,'p_binary_operators','SinBot.py',28),
  ('expression -> term','expression',1,'p_expression_term','SinBot.py',41),
  ('term -> factor','term',1,'p_term_factor','SinBot.py',45),
  ('factor -> TkNum','factor',1,'p_factor_num','SinBot.py',49),
  ('factor -> TkParAbre expression TkParCierra','factor',3,'p_factor_expr','SinBot.py',53),
  ('comp_bin -> factor TkMenor factor','comp_bin',3,'p_comparador_bin','SinBot.py',57),
  ('comp_bin -> factor TkMenorIgual factor','comp_bin',3,'p_comparador_bin','SinBot.py',58),
  ('comp_bin -> factor TkMayor factor','comp_bin',3,'p_comparador_bin','SinBot.py',59),
  ('comp_bin -> factor TkMayorIgual factor','comp_bin',3,'p_comparador_bin','SinBot.py',60),
]
