var calc = {
    codes: {
        0:"0",
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9",
        10:".",
        11:"-",
        12:"+",
        13:"*",
        14:"/",
        15:"Math.tan(",
        16:"Math.cos(",
        17:"Math.sin(",
    },
    special_mode: 0,
    input: function (input) {
        if(input === 15 || input === 16 || input === 17){
            this.special_mode = 1;
        }
        else if((input === 11 || input === 12 || input === 13 || input === 14) && this.special_mode === 1){
            this.special_mode = 0;
            document.getElementById('formula_box').value += ")"
        }
        document.getElementById('formula_box').value += this.codes[input];
    },

    back: function () {
        document.getElementById('formula_box').value=document.getElementById('formula_box').value.substring(0,document.getElementById('formula_box').value.length-1);
    },

    solve: function() {
        // HELLA insecure but it works :)
        document.getElementById('formula_box').value=eval(document.getElementById('formula_box').value);
    },

    clear: function() {
        document.getElementById('formula_box').value="";
        this.special_mode = 0;
    }
}