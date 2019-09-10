def asteroidCollision(asteroids):
    for(i,j in range(0,len(asteroids):
        for(; j > 0 && asteroids[j - 1] > 0 && asteroids[j - 1] < -asteroids[i]; j --);
        if(j == 0 || asteroids[i] > 0 || asteroids[j - 1] < 0){
        asteroids[j ++] = asteroids[i];
        }else if(asteroids[i] == -asteroids[j - 1]) {
        j --;
        }
        }
    return Arrays.copyOf(asteroids, j);


# USE Stack NGE