# Demonstração do Agente de IA para Atendimento de Farmácia

Este documento apresenta uma demonstração do funcionamento do Agente de IA para Atendimento de Farmácia em diferentes cenários de uso.

## Cenários de Demonstração

### 1. Saudação e Apresentação

**Plataforma:** Telegram e WhatsApp

**Descrição:** O usuário inicia uma conversa com o bot.

**Interação:**

```
Usuário: Olá

Bot: Olá! Bem-vindo à Farmácia Virtual. Como posso ajudar você hoje? 😊

Posso fornecer informações sobre medicamentos, verificar disponibilidade de produtos, informar horários de funcionamento e muito mais.
```

### 2. Consulta de Horário de Funcionamento

**Plataforma:** Telegram

**Descrição:** O usuário utiliza o comando para verificar o horário de funcionamento.

**Interação:**

```
Usuário: /horario

Bot: Nossa farmácia está aberta nos seguintes horários:

Segunda a Sexta: 08:00 às 20:00
Sábados: 08:00 às 18:00
Domingos e Feriados: 09:00 às 13:00

Posso ajudar com mais alguma informação?
```

**Plataforma:** WhatsApp

**Descrição:** O usuário pergunta sobre o horário de funcionamento.

**Interação:**

```
Usuário: Que horas vocês fecham?

Bot: Nossa farmácia está aberta nos seguintes horários:

Segunda a Sexta: 08:00 às 20:00
Sábados: 08:00 às 18:00
Domingos e Feriados: 09:00 às 13:00

Posso ajudar com mais alguma informação?
```

### 3. Consulta de Localização

**Plataforma:** Telegram

**Descrição:** O usuário utiliza o comando para verificar a localização da farmácia.

**Interação:**

```
Usuário: /localizacao

Bot: Nossa farmácia está localizada na Av. Principal, 123 - Centro.

Referência: Próximo ao Banco do Brasil.

Você pode nos encontrar facilmente pelo Google Maps pesquisando por 'Farmácia Virtual'.
```

**Plataforma:** WhatsApp

**Descrição:** O usuário pergunta sobre a localização da farmácia.

**Interação:**

```
Usuário: Onde fica a farmácia?

Bot: Nossa farmácia está localizada na Av. Principal, 123 - Centro.

Referência: Próximo ao Banco do Brasil.

Você pode nos encontrar facilmente pelo Google Maps pesquisando por 'Farmácia Virtual'.
```

### 4. Informações sobre Medicamentos

**Plataforma:** Telegram e WhatsApp

**Descrição:** O usuário pergunta sobre um medicamento específico.

**Interação:**

```
Usuário: Para que serve o Paracetamol?

Bot: Você gostaria de informações sobre Paracetamol. Estou buscando os detalhes para você...

[Após processamento]

Bot: Aqui estão as informações sobre Paracetamol:

- Indicação: Analgésico e antitérmico indicado para dores leves a moderadas e febre.
- Posologia: Adultos e crianças acima de 12 anos: 1 comprimido de 500mg a 750mg a cada 4 a 6 horas, não excedendo 4g por dia.
- Efeitos colaterais: Raramente causa efeitos colaterais quando usado nas doses recomendadas. Em alguns casos, pode causar reações alérgicas leves.
- Contraindicações: Pacientes com hipersensibilidade ao paracetamol ou a qualquer componente da fórmula. Pacientes com doença hepática grave.

Posso ajudar com mais alguma informação sobre este medicamento?
```

### 5. Verificação de Disponibilidade

**Plataforma:** Telegram e WhatsApp

**Descrição:** O usuário pergunta sobre a disponibilidade de um medicamento.

**Interação:**

```
Usuário: Vocês têm Omeprazol?

Bot: Você gostaria de verificar a disponibilidade de Omeprazol. Estou consultando nosso estoque...

[Após processamento]

Bot: Verificamos e temos Omeprazol disponível em estoque! Deseja saber o preço ou mais informações sobre este produto?

Usuário: Qual o preço?

Bot: O preço atual de Omeprazol é R$ 12,30. Posso ajudar com mais alguma informação?
```

### 6. Recomendação para Sintomas

**Plataforma:** Telegram e WhatsApp

**Descrição:** O usuário descreve um sintoma e recebe recomendações.

**Interação:**

```
Usuário: Estou com dor de cabeça

Bot: Entendi que você está com dor de cabeça. Pode me dar mais detalhes sobre esse sintoma? Por exemplo, há quanto tempo está sentindo, se há outros sintomas associados, etc.

Usuário: Começou hoje de manhã, é uma dor latejante na testa

Bot: Para sintomas como 'dor de cabeça latejante na testa', posso recomendar:

1. Paracetamol - Analgésico para dores leves a moderadas
2. Dipirona - Analgésico e antitérmico
3. Ibuprofeno - Anti-inflamatório não esteroidal

Lembre-se que esta é apenas uma sugestão inicial. Para um diagnóstico preciso, consulte um médico ou farmacêutico.
```

### 7. Solicitação de Atendimento Humano

**Plataforma:** Telegram

**Descrição:** O usuário solicita falar com um atendente humano.

**Interação:**

```
Usuário: /falar_humano

Bot: Entendo que você prefere falar com um atendente humano.

Para isso, você pode ligar para nossa central de atendimento no número (XX) XXXX-XXXX ou enviar um e-mail para atendimento@farmaciavirtual.com.br.

Nosso horário de atendimento humano é de segunda a sexta, das 8h às 18h.
```

**Plataforma:** WhatsApp

**Descrição:** O usuário solicita falar com um atendente humano.

**Interação:**

```
Usuário: Quero falar com um atendente

Bot: Entendo que você prefere falar com um atendente humano.

Para isso, você pode ligar para nossa central de atendimento no número (XX) XXXX-XXXX ou enviar um e-mail para atendimento@farmaciavirtual.com.br.

Nosso horário de atendimento humano é de segunda a sexta, das 8h às 18h.
```

### 8. Despedida

**Plataforma:** Telegram e WhatsApp

**Descrição:** O usuário se despede do bot.

**Interação:**

```
Usuário: Obrigado, tchau

Bot: Obrigado por entrar em contato! Estamos sempre à disposição para ajudar. Tenha um ótimo dia! 👋
```

## Fluxos de Conversação Complexos

### Fluxo 1: Consulta de Medicamento e Disponibilidade

**Plataforma:** Telegram e WhatsApp

**Descrição:** O usuário pergunta sobre um medicamento e depois verifica sua disponibilidade.

**Interação:**

```
Usuário: Para que serve Dipirona?

Bot: Você gostaria de informações sobre Dipirona. Estou buscando os detalhes para você...

Bot: Aqui estão as informações sobre Dipirona:

- Indicação: Analgésico, antitérmico e antiespasmódico indicado para dores e febre.
- Posologia: Adultos e crianças acima de 12 anos: 1 comprimido de 500mg a 1g a cada 6 a 8 horas, não excedendo 4g por dia.
- Efeitos colaterais: Pode causar reações alérgicas, queda de pressão e, raramente, alterações sanguíneas.
- Contraindicações: Pacientes com hipersensibilidade à dipirona ou a qualquer componente da fórmula, com deficiência de G6PD, porfiria hepática ou granulocitopenia.

Posso ajudar com mais alguma informação sobre este medicamento?

Usuário: Vocês têm esse medicamento disponível?

Bot: Verificamos e temos Dipirona disponível em estoque! Deseja saber o preço ou mais informações sobre este produto?

Usuário: Qual o preço?

Bot: O preço atual de Dipirona é R$ 4,50. Posso ajudar com mais alguma informação?

Usuário: Não, obrigado

Bot: Por nada! Estou aqui para ajudar. Precisa de mais alguma coisa?
```

### Fluxo 2: Sintoma, Recomendação e Verificação de Disponibilidade

**Plataforma:** Telegram e WhatsApp

**Descrição:** O usuário descreve um sintoma, recebe recomendações e verifica a disponibilidade de um dos medicamentos recomendados.

**Interação:**

```
Usuário: Estou com febre alta

Bot: Entendi que você está com febre. Pode me dar mais detalhes sobre esse sintoma? Por exemplo, há quanto tempo está sentindo, se há outros sintomas associados, etc.

Usuário: Começou ontem à noite, estou com 38,5°C de febre e dor no corpo

Bot: Para sintomas como 'febre alta e dor no corpo', posso recomendar:

1. Paracetamol - Analgésico e antitérmico para febre e dores leves a moderadas
2. Dipirona - Analgésico e antitérmico potente
3. Ibuprofeno - Anti-inflamatório não esteroidal que também ajuda a reduzir a febre

Lembre-se que esta é apenas uma sugestão inicial. Para um diagnóstico preciso, consulte um médico ou farmacêutico.

Usuário: Vocês têm Paracetamol?

Bot: Verificamos e temos Paracetamol disponível em estoque! Deseja saber o preço ou mais informações sobre este produto?

Usuário: Qual o preço?

Bot: O preço atual de Paracetamol é R$ 5,99. Posso ajudar com mais alguma informação?
```

## Conclusão

Esta demonstração ilustra as principais funcionalidades do Agente de IA para Atendimento de Farmácia, mostrando como ele pode auxiliar os clientes em diferentes cenários. O bot é capaz de:

1. Responder a perguntas frequentes sobre a farmácia
2. Fornecer informações detalhadas sobre medicamentos
3. Verificar a disponibilidade de produtos
4. Recomendar medicamentos com base em sintomas
5. Direcionar o usuário para um atendente humano quando necessário

O bot está disponível tanto no Telegram quanto no WhatsApp, oferecendo uma experiência consistente em ambas as plataformas.

