//Built a object to iterate them with for in loop
const elementTypes = {
    gallium : 'Liquid',
    aluminum : 'Solid',
    iron : 'Metal',
    hydrogen : 'Gas',
    helium : 'Gas',
    lithium : 'Solid',
    beryllium : 'Solid',
    carbon : 'Solid',
    nitrogen : 'Gas',
    oxygen : 'Gas',
    fluorine : 'Gas',
    neon : 'Gas',
    sodium : 'Solid',
    magnesium : 'Solid',
    silicon : 'Solid',
    sulfur : 'Solid',
    germanium : 'Solid',
    potassium : 'Solid',
    rubidium : 'Solid',
    caesium : 'Solid',
    francium : 'Solid',
    curium : 'Solid',
    dubnium : 'Solid',
}

for(let element in elementTypes){
    console.log(element + " is " + elementTypes[element]+ " in room temperature")
}