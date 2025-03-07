BEGIN{
    v_num = 0
    exactly_one = 0
    colours[1] = "Red"
    colours[2] = "Black"
    colours[3] = "White"
    retStr = ""
}
{
    if(NF ~ 1){
        v_num = $1
    }
    if(NF>1){
        if (exactly_one ~ 0){
            for(i = 1; i<=v_num;i++){
                printf "(v%s%s|v%s%s|v%s%s)&", i,colours[1], i,colours[2],i,colours[3]
                printf "(~v%s%s|~v%s%s)&", i,colours[1], i,colours[2]
                printf "(~v%s%s|~v%s%s)&", i,colours[1], i,colours[3]
                printf "(~v%s%s|~v%s%s)&", i,colours[3], i,colours[2]
            }
            exactly_one = 1
        }
        if (retStr ~ /)/){
            printf "&"
        }
        printf "(~v%s%s|~v%s%s)&", $1,colours[1], $3,colours[1]
        printf "(~v%s%s|~v%s%s)&", $1,colours[2], $3,colours[2]
        printf "(~v%s%s|~v%s%s)", $1,colours[3], $3,colours[3]
        retStr = ")"
    }
}
