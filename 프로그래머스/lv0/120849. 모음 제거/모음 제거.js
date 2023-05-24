function solution(my_string) {
    let answer = '';
    Array.from(my_string).forEach(v => ['a','e','i','o','u'].includes(v)||(answer += v))
    return answer;
}