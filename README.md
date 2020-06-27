# conjugaime
Uma api python que conjuga verbos


#### Metas:

- Indicativo `(OK com verbos regulares)`
- Conjuntivo
- Imperativo

#### Observações:

- [x] Verbo "xurugar" veio sem o "u" em "xurug**u**ei" (1ª pess. do pret. perf. do ind.). Consertar


- Tem que ver se `self.sufixo = verbo[-2:]` vai se comportar bem com morfemas com mais de duas letras, como "-mos". Se esse atributo receber apenas verbos auxiliares no infinitivo, então ignora esse comentário. Tô apenas perscrutando o código.

- Existe uma classe quase que excepcional de verbos da 4ª conjugação: os terminados em `-or`

  ```python
  if self.sufixo not in ['ar','er','ir']:
              print("Sua palavra não é um verbo")
  
  ```

* Peguei uma lista de 301 verbos irregulares do português. Não sei se a lista é fechada mesmo (averiguar). 
  * Uma subtask é inserir todos os 301 e a lista com suas conjugações. Mas ainda não porque talvez algumas coisas (que não sei quais são) precisem ser otimizadas antes. Standby.

