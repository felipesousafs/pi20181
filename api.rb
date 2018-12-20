require 'rest-client'

pokemon_name = 'gengar'

get_pokemon = RestClient.get "https://pokeapi.co/api/v2/pokemon/#{pokemon_name}"

puts get_pokemon.body
