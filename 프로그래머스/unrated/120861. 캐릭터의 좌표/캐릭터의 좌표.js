function solution(keyinput, board) {
    let [x, y] = [0, 0]
    let boundary = [Math.floor(board[0]/2), Math.floor(board[1]/2)]
    
    for (let order of keyinput){
        switch(order){
            case "up": 
                if (y<boundary[1]) {y++};
                break;
            case "down":
                if (y>-boundary[1]) {y--};
                break;
            case "left":
                if (x>-boundary[0]) {x--};
                break;
            case "right":
                if (x<boundary[0]) {x++};
                break;
        }
    }

    return [x, y];
}