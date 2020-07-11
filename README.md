# Conjugai-Me
Este projeto é um fork do [conjugai-me](https://github.com/dunossauro/conjugai-me) do [Eduardo Mendes](https://github.com/dunossauro): uma API Python que conjuga verbos em português.


#### TODO:

- Modo Indicativo
  - Verbos regulares (DONE!)
  - Verbos irregulares (TODO)
- Modo Conjuntivo/Subjuntivo
  - **Verbos regulares (DOING)**
  - Verbos irregulares (TODO)
- Modo Imperativo
  - Verbos regulares (TODO)
  - Verbos irregulares (TODO)
- Indicativo
- Conjuntivo
- Imperativo
- Refinar a API
- Adicionar todos os verbos irregulares


## Desenvolvimento

O projeto usa Poetry para gerenciar a instalação dos pacotes e o tox como test-runner

### Rodar os testes e a cobertura
```bash
tox
```


### Ver a cobertura dos testes
```bash
tox -e cov
```

> Caso algum teste quebre os resultados não estarão disponiveis

### Para ver a cobertura no browser

```bash
firefox htmlcov/index.html
```

#### Checklist/Roadmap
- [x] Verbo "xurugar" veio sem o "u" em "xurug**u**ei" (1ª pess. do pret. perf. do ind.). Consertar
- [ ] Consertar o tamanho do slice dos radicais na classe `Subjuntivo()`
- [ ] Escrever testes para outras pessoas do verbo além da 1ª
- [ ] Escrever testes para verbos com radicais terminados em `-g`, como "xurugar"



#### Observações
- Tem que ver se `self.sufixo = verbo[-2:]` vai se comportar bem com morfemas com mais de duas letras, como "-mos". Se esse atributo receber apenas verbos auxiliares no infinitivo, então ignora esse comentário. Tô apenas perscrutando o código.

- Existe uma classe quase que excepcional de verbos da 4ª conjugação: os terminados em `-or`

  ```python
  if self.sufixo not in ['ar','er','ir']:
              print("Sua palavra não é um verbo")
  ```

* Peguei uma lista de **301** verbos irregulares do português. Não sei se a lista é fechada mesmo (averiguar). 
  
  * Uma subtask é inserir todos os 301 e a lista com suas conjugações. Mas ainda não porque talvez algumas coisas (que não sei quais são) precisem ser otimizadas antes. Standby.





