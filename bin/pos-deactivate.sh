#!/usr/bin/env bash

# Impressao formatada de informacao no log
function print_info () {
	printf "[%s %s] INFO - %s\n" "$(date +%d-%m-%Y)" "$(date +%H:%M:%S)" "$1"
}


# Impressao formatada de erro no log
function print_erro () {
    printf "[%s %s] ERRO - %s\n" "$(date +%d-%m-%Y)" "$(date +%H:%M:%S)" "$1"
}


function main () {

    print_info "Removendo as variaveis no ambiente."
    unset TELEGRAM_TOKEN=valor
    print_info "Variaveis removidas."

}

main "$@"
