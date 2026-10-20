# =====================================================================
#  SOLUÇÕES — os 14 exercícios do Rank 03 (Python)
# =====================================================================
#
#  Corre:   python3 solucoes_rank03.py
#  (os testes no fim confirmam que as 14 dão OK)
#
#  Estão pela ordem do site, do nível 1 ao nível 6, e já seguem as
#  regras do site de outubro de 2026.
#  Cada exercício tem:  o que pede  /  a ideia  /  o código.
#
#  Como estudar: lê a "Ideia", tapa o código e tenta escrevê-lo.
#  Só depois compara. Não abras isto a meio de um exame de treino.
#  Para praticar, escreve noutro ficheiro, e não neste.
#
#  As funções auxiliares estão sempre logo acima da função que as usa.
#  No exame vão no mesmo ficheiro que a função pedida.
#
#  Os padrões que se repetem:
#    Pilha ................................ 01
#    Ordenar à mão (inserção) ............. 02
#    Limpar primeiro, comparar depois ..... 03, 09
#    Construir uma string/lista nova ...... 04, 06, 12, 14
#    Dois índices ......................... 05, 10
#    Vizinhos (i e i + 1) ................. 08
#    Contar ou ordenar as letras .......... 09, 11
#    Contas com %, //, ord e chr .......... 07, 13, 14
#
# =====================================================================
#  01 — py_bracket_validator   (nível 1, fácil)
# =====================================================================
#  Pede: True se os parênteses (), [] e {} abrem e fecham pela ordem
#        certa. Os outros caracteres são ignorados.
#     "{[]}" -> True      "([)]" -> False      "((" -> False
#
#  Ideia: pilha. Quem abre vai para a pilha; quem fecha tem de
#  encontrar o seu par no topo. No fim a pilha tem de estar vazia.
def bracket_validator(s: str) -> bool:
    pares = {")": "(", "]": "[", "}": "{"}      # quem fecha -> quem abre
    pilha = []
    for c in s:
        if c in "([{":
            pilha.append(c)
        elif c in pares:
            # fechou sem nada aberto, ou o último aberto não é o par
            if not pilha or pilha[-1] != pares[c]:
                return False
            pilha.pop()
    return len(pilha) == 0


# =====================================================================
#  02 — py_cryptic_sorter   (nível 1, fácil)
# =====================================================================
#  Pede: ordenar strings por 1) tamanho, 2) ordem alfabética sem
#        distinguir maiúsculas, 3) número de vogais. As que empatam
#        em tudo ficam pela ordem em que vinham.
#     ["aaa", "bbb", "AAA", "BBB"] -> ["aaa", "AAA", "bbb", "BBB"]
#  PROIBIDO: sorted() e list.sort()
#
#  Ideia: ordenar à mão, por inserção. Vais construindo o resultado
#  já ordenado: cada string entra logo a seguir a todas as que vêm
#  antes dela ou empatam com ela. Para comparar usa-se um tuplo, um
#  elemento por regra (o Python só olha para o seguinte se empatar).
#  É o <= que deixa os empates pela ordem original ("aaa" vinha
#  antes de "AAA", por isso fica antes).
def conta_vogais(s: str) -> int:
    total = 0
    for c in s:
        if c in "aeiouAEIOU":
            total += 1
    return total


def criterio_cryptic(s: str) -> tuple:
    return (len(s), s.lower(), conta_vogais(s))


def cryptic_sorter(strings: list[str]) -> list[str]:
    resultado = []
    for s in strings:
        chave = criterio_cryptic(s)
        i = 0
        # passa à frente de todas as que vêm antes de s ou empatam com ela
        while i < len(resultado) and criterio_cryptic(resultado[i]) <= chave:
            i += 1
        resultado.insert(i, s)                  # põe s na posição i
    return resultado


# =====================================================================
#  03 — py_echo_validator   (nível 2, fácil)
# =====================================================================
#  Pede: True se for palíndromo, olhando só para as letras e sem
#        distinguir maiúsculas.
#     "A man a plan a canal Panama" -> True      "" -> False
#
#  Ideia: dois passos. 1) limpar: ficar só com as letras, em
#  minúsculas. 2) comparar com ela própria invertida.
#  Cuidado: se não sobrar letra nenhuma, a resposta é False.
def echo_validator(text: str) -> bool:
    limpa = ""
    for c in text:
        if c.isalpha():
            limpa += c.lower()
    if not limpa:
        return False
    return limpa == limpa[::-1]


# =====================================================================
#  04 — py_mirror_matrix   (nível 2, fácil)
# =====================================================================
#  Pede: uma matriz nova com cada linha invertida.
#     [[1, 2, 3], [4, 5, 6]] -> [[3, 2, 1], [6, 5, 4]]
#
#  Ideia: percorrer as linhas e guardar cada uma invertida numa
#  matriz nova. O [::-1] cria uma lista nova, não mexe na original.
def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    nova = []
    for linha in matrix:
        nova.append(linha[::-1])
    return nova


# =====================================================================
#  05 — py_hidenp   (nível 3, médio)
# =====================================================================
#  Pede: True se todas as letras de small aparecem em big pela mesma
#        ordem (pode haver outras pelo meio).
#     ("abc", "a1b2c3") -> True      ("aec", "abcde") -> False
#
#  Ideia: dois índices. O de big anda sempre; o de small só anda
#  quando encontra a letra que procura. No fim: small chegou ao fim?
def hidenp(small: str, big: str) -> bool:
    i = 0                       # onde vou em small
    j = 0                       # onde vou em big
    while i < len(small) and j < len(big):
        if small[i] == big[j]:
            i += 1
        j += 1
    return i == len(small)


# =====================================================================
#  06 — py_inter   (nível 3, médio)
# =====================================================================
#  Pede: os caracteres que estão nas duas strings, sem repetir, pela
#        ordem em que aparecem na primeira.
#     ("banana", "band") -> "ban"      ("abc", "xyz") -> ""
#
#  Ideia: percorrer s1 e fazer duas perguntas a cada caractere:
#  está em s2? ainda não o pus no resultado?
def inter(s1: str, s2: str) -> str:
    resultado = ""
    for c in s1:
        if c in s2 and c not in resultado:
            resultado += c
    return resultado


# =====================================================================
#  07 — py_number_base_converter   (nível 3, médio)
# =====================================================================
#  Pede: converter um número (string) de uma base para outra.
#        Bases de 2 a 36; dígitos 0-9 e A-Z. "ERROR" se for inválido.
#     ("FF", 16, 10) -> "255"       ("255", 10, 16) -> "FF"
#     ("G", 16, 10) -> "ERROR"      ("123", 1, 10) -> "ERROR"
#
#  Ideia: dois passos, a passar sempre por um inteiro normal.
#  1) string -> inteiro:  valor = valor * base + dígito
#     (o de_binario da Aula 04, com a base em vez do 2)
#  2) inteiro -> string:  restos de % base, juntos à ESQUERDA
#     (o para_binario da Aula 04)
#  A posição de cada caractere em DIGITOS é o valor desse dígito.
#  Cuidado: o enunciado não fala de minúsculas nem de negativos.
#  Aqui "ff" é aceite como "FF", e o "-" dá ERROR.
DIGITOS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "ERROR"
    if number == "":
        return "ERROR"

    # 1) da base de origem para inteiro
    validos = DIGITOS[:from_base]           # os dígitos que esta base aceita
    valor = 0
    for c in number.upper():
        if c not in validos:
            return "ERROR"
        valor = valor * from_base + validos.index(c)    # index = posição de c

    # 2) de inteiro para a base de destino
    if valor == 0:                          # o while de baixo nem entrava
        return "0"
    resultado = ""
    while valor > 0:
        resultado = DIGITOS[valor % to_base] + resultado
        valor = valor // to_base
    return resultado


# =====================================================================
#  08 — py_pattern_tracker   (nível 3, médio)
# =====================================================================
#  Pede: contar os pares de dígitos VIZINHOS em que o segundo é o
#        primeiro mais 1. O 9 seguido de 0 não conta.
#     "123" -> 2      "12a34" -> 2      "1a2b3c4" -> 0      "112233" -> 2
#
#  Ideia: olhar para cada caractere e para o seguinte (i e i + 1).
#  O i só vai até ao penúltimo, senão o i + 1 sai da string.
#  O caso "90" resolve-se sozinho: 0 não é igual a 9 + 1.
def pattern_tracker(text: str) -> int:
    total = 0
    for i in range(len(text) - 1):
        a = text[i]
        b = text[i + 1]
        if a.isdigit() and b.isdigit() and int(b) == int(a) + 1:
            total += 1
    return total


# =====================================================================
#  09 — py_anagram   (nível 4, médio)
# =====================================================================
#  Pede: True se as duas strings têm as mesmas letras nas mesmas
#        quantidades, sem contar espaços nem distinguir maiúsculas.
#     ("Dormitory", "Dirty Room") -> True      ("abc", "abcc") -> False
#
#  Ideia: contar as letras de cada string num dicionário (tudo em
#  minúsculas, a saltar os espaços) e comparar os dois com ==.
def conta_letras(s: str) -> dict:
    conta = {}
    for c in s.lower():
        if c != " ":
            conta[c] = conta.get(c, 0) + 1
    return conta


def anagram(s1: str, s2: str) -> bool:
    return conta_letras(s1) == conta_letras(s2)


# =====================================================================
#  10 — py_shadow_merge   (nível 4, médio)
# =====================================================================
#  Pede: juntar duas listas já ordenadas numa só lista ordenada.
#     ([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
#
#  Ideia: dois índices. Em cada passo vai para o resultado o menor
#  dos dois da frente, e só esse índice avança. Quando uma lista
#  acaba, o que sobrou da outra já está ordenado: junta-se no fim.
#  (No exame, return sorted(list1 + list2) também passa.)
def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    i = 0
    j = 0
    resultado = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            resultado.append(list1[i])
            i += 1
        else:
            resultado.append(list2[j])
            j += 1
    return resultado + list1[i:] + list2[j:]    # uma destas fatias vem vazia


# =====================================================================
#  11 — py_string_permutation_checker   (nível 4, médio)
# =====================================================================
#  Pede: True se uma string é a outra com os caracteres noutra ordem.
#        Aqui TUDO conta: maiúsculas, espaços e pontuação.
#     ("abc", "bca") -> True      ("Abc", "abc") -> False      ("", "") -> True
#
#  Ideia: se ordenares os caracteres das duas e ficarem iguais, têm
#  os mesmos caracteres nas mesmas quantidades.
#  (Também dá com dicionários, como no anagram. E o anagram também
#  dá com sorted, depois de limpar as strings.)
def string_permutation_checker(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)             # sorted("bca") -> ["a", "b", "c"]


# =====================================================================
#  12 — py_string_sculptor   (nível 5, difícil)
# =====================================================================
#  Pede: alternar minúscula/maiúscula só nas letras, a começar em
#        minúscula. O que não é letra (espaços incluídos) fica igual
#        e não conta para a alternância.
#     "Hello World" -> "hElLo WoRlD"      "abc123def" -> "aBc123DeF"
#  Mudou no site: os espaços já NÃO fazem recomeçar a alternância.
#
#  Ideia: um contador de letras. Par -> minúscula, ímpar -> maiúscula.
#  Só as letras fazem andar o contador.
def string_sculptor(text: str) -> str:
    resultado = ""
    n = 0                       # quantas letras já vi
    for c in text:
        if c.isalpha():
            if n % 2 == 0:
                resultado += c.lower()
            else:
                resultado += c.upper()
            n += 1
        else:
            resultado += c
    return resultado


# =====================================================================
#  13 — py_twist_sequence   (nível 5, difícil)
# =====================================================================
#  Pede: rodar a lista k posições para a direita (os últimos k passam
#        para o início).
#     ([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]      ([1, 2, 3], 5) -> [2, 3, 1]
#
#  Ideia: 1) tirar as voltas completas com %;  2) achar o ponto de
#  corte, a contar do fim;  3) trocar os dois bocados de sítio.
#  Cuidado: a lista vazia vem primeiro, senão o % divide por 0.
def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    k = k % len(arr)
    corte = len(arr) - k
    return arr[corte:] + arr[:corte]


# =====================================================================
#  14 — py_whisper_cipher   (nível 6, difícil)
# =====================================================================
#  Pede: cifra de César. Cada letra anda shift posições no alfabeto,
#        a dar a volta. O que não é letra fica igual. O shift pode
#        ser negativo.
#     ("xyz", 3) -> "abc"      ("Hello World!", 1) -> "Ifmmp Xpsme!"
#
#  Ideia: para cada letra: tirar a base (fica de 0 a 25), somar o
#  shift, % 26 para dar a volta, e voltar a somar a base.
#  A base é ord("a") nas minúsculas e ord("A") nas maiúsculas.
def roda_letra(c: str, base: int, shift: int) -> str:
    posicao = ord(c) - base                 # 0 a 25
    posicao = (posicao + shift) % 26        # anda e dá a volta
    return chr(posicao + base)              # volta a ser letra


def whisper_cipher(text: str, shift: int) -> str:
    resultado = ""
    for c in text:
        if "a" <= c <= "z":                 # como c >= 'a' && c <= 'z' em C
            resultado += roda_letra(c, ord("a"), shift)
        elif "A" <= c <= "Z":
            resultado += roda_letra(c, ord("A"), shift)
        else:
            resultado += c
    return resultado


# =====================================================================
#  TESTES — não mexas daqui para baixo
# =====================================================================
def _testa(nome, func, casos):
    ok = True
    for args, esperado in casos:
        try:
            obtido = func(*args)
        except Exception as e:
            obtido = f"ERRO: {type(e).__name__} {e}"
        if obtido != esperado:
            ok = False
            print(f"  KO {nome}{args} -> {obtido!r}  (esperado {esperado!r})")
    print(f"{'OK' if ok else 'KO'}  {nome}")
    return ok


def _testes():
    todos = [
        ("bracket_validator", bracket_validator, [
            (("()",), True), (("()[]{}",), True), (("(]",), False),
            (("([)]",), False), (("{[]}",), True), (("hello(world)",), True),
            (("((())",), False), (("",), True), (("]",), False),
            (("((",), False), (("}{",), False), (("{[()]}",), True),
            (("abc",), True), (("a]",), False), (("(()))",), False),
        ]),
        ("cryptic_sorter", cryptic_sorter, [
            ((["apple", "cat", "banana", "dog", "elephant"],),
             ["cat", "dog", "apple", "banana", "elephant"]),
            ((["aaa", "bbb", "AAA", "BBB"],), ["aaa", "AAA", "bbb", "BBB"]),
            ((["hello", "world", "hi", "test"],), ["hi", "test", "hello", "world"]),
            (([],), []), (([""],), [""]), ((["b", "a"],), ["a", "b"]),
            ((["B", "a"],), ["a", "B"]), ((["a", "A"],), ["a", "A"]),
            ((["bb", "a", "ccc", "dd"],), ["a", "bb", "dd", "ccc"]),
            ((["Zeta", "alfa", "Beta"],), ["alfa", "Beta", "Zeta"]),
            ((["x", "x", ""],), ["", "x", "x"]),
            ((["bA", "Ba"],), ["bA", "Ba"]),
            ((["B", "b", "a", "A"],), ["a", "A", "B", "b"]),
        ]),
        ("echo_validator", echo_validator, [
            (("racecar",), True), (("A man a plan a canal Panama",), True),
            (("race a car",), False), (("Was it a car or a cat I saw",), True),
            (("hello",), False), (("Madam Im Adam",), True), (("",), False),
            (("madam",), True), (("Able was I ere I saw Elba",), True),
            (("a",), True), (("Ab",), False), (("No lemon, no melon",), True),
            (("Aa",), True), (("abca",), False),
        ]),
        ("mirror_matrix", mirror_matrix, [
            (([[1, 2, 3], [4, 5, 6]],), [[3, 2, 1], [6, 5, 4]]),
            (([[1, 2], [3, 4], [5, 6]],), [[2, 1], [4, 3], [6, 5]]),
            (([[7]],), [[7]]), (([[1, 2, 3, 4]],), [[4, 3, 2, 1]]),
            (([[-1, -2], [-3, -4]],), [[-2, -1], [-4, -3]]),
            (([],), []), (([[]],), [[]]), (([[1], [2]],), [[1], [2]]),
            (([[1, 2, 3], [4]],), [[3, 2, 1], [4]]),
        ]),
        ("hidenp", hidenp, [
            (("abc", "a1b2c3"), True), (("ace", "abcde"), True),
            (("aec", "abcde"), False), (("", "abc"), True),
            (("abc", "ab"), False), (("aaaa", "aaa"), False),
            (("sing", "subsequence testing"), True), (("", ""), True),
            (("a", ""), False), (("Abc", "abc"), False),
            (("abc", "abc"), True), (("ba", "ab"), False),
        ]),
        ("inter", inter, [
            (("hello", "world"), "lo"), (("banana", "band"), "ban"),
            (("abcabc", "bc"), "bc"), (("abc", "xyz"), ""), (("", "abc"), ""),
            (("abc", ""), ""), (("abc", "abc"), "abc"), (("aab", "a"), "a"),
            (("AbC", "abc"), "b"), (("hello world", "o l"), "lo "),
            (("cba", "abc"), "cba"),
        ]),
        ("number_base_converter", number_base_converter, [
            (("1010", 2, 10), "10"), (("FF", 16, 10), "255"),
            (("255", 10, 16), "FF"), (("123", 10, 2), "1111011"),
            (("Z", 36, 10), "35"), (("35", 10, 36), "Z"),
            (("123", 1, 10), "ERROR"), (("G", 16, 10), "ERROR"),
            (("0", 10, 2), "0"), (("10", 10, 37), "ERROR"),
            (("2", 2, 10), "ERROR"), (("", 10, 2), "ERROR"),
            (("007", 10, 10), "7"), (("ZZ", 36, 2), "10100001111"),
            (("ff", 16, 10), "255"), (("-5", 10, 2), "ERROR"),
        ]),
        ("pattern_tracker", pattern_tracker, [
            (("123",), 2), (("12a34",), 2), (("987654321",), 0),
            (("01234567",), 7), (("abc",), 0), (("1a2b3c4",), 0),
            (("112233",), 2), (("",), 0), (("5",), 0), (("90",), 0),
            (("89",), 1), (("8910",), 1), (("0123456789",), 9),
            (("12 34",), 2),
        ]),
        ("anagram", anagram, [
            (("listen", "silent"), True), (("Triangle", "Integral"), True),
            (("Dormitory", "Dirty Room"), True), (("hello", "world"), False),
            (("", ""), True), (("abc", "abcc"), False), (("a", "A"), True),
            (("ab", "a b"), True), (("aab", "abb"), False),
            (("  ", ""), True), (("abc", "abd"), False),
            (("Listen", "Silent "), True), (("a", ""), False),
        ]),
        ("shadow_merge", shadow_merge, [
            (([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]),
            (([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6]),
            (([1], [2, 3, 4]), [1, 2, 3, 4]), (([], [1, 2, 3]), [1, 2, 3]),
            (([1, 1, 2], [1, 3, 3]), [1, 1, 1, 2, 3, 3]), (([], []), []),
            (([1, 2, 3], []), [1, 2, 3]), (([5], [1, 2]), [1, 2, 5]),
            (([-3, 0], [-5, -1, 2]), [-5, -3, -1, 0, 2]),
            (([4, 5, 6], [1, 2, 3]), [1, 2, 3, 4, 5, 6]),
        ]),
        ("string_permutation_checker", string_permutation_checker, [
            (("abc", "bca"), True), (("abc", "def"), False),
            (("listen", "silent"), True), (("hello", "bello"), False),
            (("", ""), True), (("a", ""), False), (("Abc", "abc"), False),
            (("a gentleman", "elegant man"), True), (("aab", "abb"), False),
            (("a b", "b a"), True), (("ab", "abc"), False),
            (("!a", "a!"), True),
        ]),
        ("string_sculptor", string_sculptor, [
            (("hello",), "hElLo"), (("Hello World",), "hElLo WoRlD"),
            (("   hello   ",), "   hElLo   "),
            (("abc123def",), "aBc123DeF"), (("Python3.9!",), "pYtHoN3.9!"),
            (("",), ""), (("HELLO",), "hElLo"), (("a b c",), "a B c"),
            (("AB CD",), "aB cD"), (("  hi",), "  hI"), (("a1b",), "a1B"),
            (("x-y z",), "x-Y z"), (("123",), "123"),
        ]),
        ("twist_sequence", twist_sequence, [
            (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]), (([1, 2, 3], 1), [3, 1, 2]),
            (([1, 2, 3, 4], 0), [1, 2, 3, 4]), (([1, 2, 3], 5), [2, 3, 1]),
            (([], 3), []), (([1], 100), [1]), (([1, 2, 3], 3), [1, 2, 3]),
            (([1, 2, 3, 4, 5], 7), [4, 5, 1, 2, 3]), (([1, 2], 1), [2, 1]),
            (([], 0), []), (([1, 2, 3], 7), [3, 1, 2]),
            (([1, 2, 3, 4], 10), [3, 4, 1, 2]),
        ]),
        ("whisper_cipher", whisper_cipher, [
            (("hello", 3), "khoor"), (("Hello World!", 1), "Ifmmp Xpsme!"),
            (("xyz", 3), "abc"), (("ABC123def", 5), "FGH123ijk"),
            (("", 10), ""), (("abc", -3), "xyz"), (("abc", 26), "abc"),
            (("abc", -29), "xyz"), (("Zz", 1), "Aa"), (("a-b", 27), "b-c"),
            (("AbC", 0), "AbC"), (("Aa", -1), "Zz"),
        ]),
    ]
    certos = 0
    for nome, func, casos in todos:
        if _testa(nome, func, casos):
            certos += 1
    print("-" * 45)
    print(f"{certos}/{len(todos)} exercícios OK")


if __name__ == "__main__":
    _testes()
