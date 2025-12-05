[default]
list:
    @just --list

get-all-inputs:
    for i in $(seq 1 20); do just get-input $i; done

get-input day:
    @curl --cookie $(cat ~/.aoc-cookie) \
        https://adventofcode.com/2025/day/{{day}}/input \
        > `printf "inputs/day%02d_input.txt" {{day}}`
