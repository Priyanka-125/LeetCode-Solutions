int maxProfit(int* prices, int pricesSize){
     int profit = 0, buy = INT_MAX;
    
    for (int i = 0; i < pricesSize; i++) {
        buy = fmin(buy, prices[i]);
        profit = fmax(profit, prices[i] - buy);
    }
    
    return profit;

}