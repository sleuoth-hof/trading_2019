def rsi_trend(rsi):
  output = "?!?!"
  length = len(rsi)
  param_rsi_low = 30
  param_rsi_high = 60
  if length > 0:
    #Erster  Wert, welcher keinen Vergleich hat
    if length == 1:
      current_rsi = rsi[0]
      if current_rsi > param_rsi_high:
        output = "Aufwaerstrend"
      elif current_rsi < param_rsi_low:
        output = "Abwaertstrend"
    #Wenn Vergleich moeglich wird:
    elif length > 1:
      current_rsi = rsi[0]
      last_rsi = rsi[length - 1]
      if current_rsi<param_rsi_high and current_rsi>param_rsi_low:
        output = "Neutraler Markt"
      if current_rsi>=param_rsi_high:
        output = "Abwaertstrend"
      if current_rsi<=param_rsi_high and last_rsi>=param_rsi_high:
        output = "Verkauf-Signal"
      if current_rsi<=param_rsi_low:
         output = "Aufwaerstrend"
      if current_rsi>=param_rsi_low and last_rsi<=param_rsi_low:
        output = "Kauf-Singal"
  return output