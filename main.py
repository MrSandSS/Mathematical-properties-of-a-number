agreements = [
    "да", "yes", "ага", "угу", "ок", "окей", "yeah", "yep", "yup",
    "конечно", "разумеется", "естественно", "безусловно", "правда",
    "точно", "верно", "согласен", "согласна", "подтверждаю",
    "ясно", "понятно", "хорошо", "ладно", "добро", "есть", "окэй",
    "канеш", "канешн", "несомненно", "не вопрос", "не проблема",
    "как скажете", "как скажешь", "как угодно", "ясен пень",
    "по-любому", "пон", "понял", "поняла", "точняк", "само собой",
    "однозначно", "в точку", "давай", "го", "айда", "запросто",
    "поехали", "сделаем", "можно", "раз", "абсолютно", "вполне",
    "всё верно", "я за", "да уж", "готово", "давай так", "почему бы и нет",
    "ничего против", "считай, что так", "считай сделано", "ну да",
    "так точно", "плюсую", "одобряю", "зашибись", "имеет место быть",
    "неспроста", "однозначно да", "сто процентов", "100%",
    "сто пудов", "наверняка", "вполне возможно", "так и есть",
    "положительно", "именно", "подходит", "годится", "ничего",
    "пойдёт", "принято", "сделка", "заключено", "по рукам", "идеально",
    "супер", "отлично", "шикарно", "нормально", "уверен", "верю",
    "всё норм", "всё пучком", "всё чётко", "так верно", "записал",
    "решено", "как договорились", "окончательно", "положительно согласен",
    # English
    "absolutely", "for sure", "of course", "definitely", "certainly", "sure",
    "yep", "yepper", "affirmative", "roger", "indeed", "right on", "no doubt",
    "totally", "agreed", "you bet", "I do", "sure thing", "got it", "understood",
    "okay", "alright", "fine", "yup", "cool", "sounds good", "done", "bet",
    "you got it", "by all means", "positive", "yes indeed", "absolutely yes",
    # Spanish
    "sí", "claro", "por supuesto", "exacto", "cierto", "de acuerdo", "vale",
    "correcto", "afirmativo", "está bien", "perfecto", "obviamente", "sin duda",
    "definitivamente", "totalmente", "sin lugar a dudas", "de acuerdo contigo",
    "claro que sí", "sin problema", "por supuesto que sí", "estoy contigo",
    "vamos", "ok", "sí señor", "sí señora", "ya está", "yo también",
    # French
    "oui", "d'accord", "bien sûr", "certainement", "exactement", "absolument",
    "tout à fait", "évidemment", "sans doute", "ok", "ça marche", "bien entendu",
    "affirmatif", "ouais", "bien", "parfait", "en effet", "oké", "naturellement",
    "clairement", "pas de problème", "je suis d'accord", "c'est bon", "impeccable",
    "absolument oui", "c'est clair",
    # German
    "ja", "sicher", "natürlich", "absolut", "auf jeden Fall", "genau", "richtig",
    "okay", "klar", "verstanden", "jawohl", "bejaht", "stimmt", "einverstanden",
    "sicherlich", "ja klar", "absolut ja", "kein Problem", "in Ordnung",
    "na klar", "du hast recht", "genau so", "hundertprozentig",
    # Italian
    "sì", "certo", "assolutamente", "ovviamente", "decisamente", "naturalmente",
    "esattamente", "giusto", "ok", "perfetto", "bene", "esatto", "senza dubbio",
    "sicuramente", "va bene", "senza problemi", "non c'è problema", "perfettamente",
    "ti seguo", "d'accordo", "tutto chiaro", "sì, certo", "sono d'accordo", "bene così",
    # Japanese
    "はい", "うん", "そうです", "もちろん", "絶対に", "間違いなく", "了解", "オーケー",
    "そうですね", "その通り", "いいですよ", "いいですね", "承知しました", "了解しました",
    "はい、もちろん", "問題ありません", "OK", "わかりました", "どうぞ", "間違いない",
    "いいね", "確かに", "その通りです", "うん、了解", "はい、大丈夫です", "はい、OK",
    # Chinese
    "是的", "当然", "绝对", "没问题", "好的", "行", "对的", "可以", "肯定", "当然可以",
    "明白", "完全同意", "好", "没错", "当然是", "好啊", "是的，没问题", "确认", "我同意",
    "完全", "一点问题没有", "对", "无疑", "没错的", "好呀", "听起来好", "没错啊"
] # list generated by chatgpt
def number_property(number):
    chars_sum = 0
    if number % 2 == 0:
        print(f'• The number {number} is even')
    else:
        print(f'• The number {number} is odd')
    print(f'• Number of digits – {len(str(number))}')
    for i in str(number):
        chars_sum += int(i)
    print(f'• Sum of digits – {chars_sum}')
    print(f'• Absolute value – {abs(number)}')
    print(f'• Square root – {number ** 0.5}')
    print(f'• Reciprocal – {1 / number}')
    print(f'• In binary system – {str(bin(number))[2:]}')
    print(f'• In octal system – {str(oct(number))[2:]}')
    print(f'• In hexadecimal system – {str(hex(number))[2:]}')


print('Type number')
print(number_property(int(input())))
