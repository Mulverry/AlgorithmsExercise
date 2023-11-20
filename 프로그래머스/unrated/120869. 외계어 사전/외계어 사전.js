function solution(spell, dic) {
    return dic.filter((el)=>spell.every((i)=>el.includes(i))).length >= 1? 1 : 2
}