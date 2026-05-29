CREATE TABLE stock_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    stock_date DATE NOT NULL,
    open_price FLOAT NOT NULL,
    high_price FLOAT NOT NULL,
    low_price FLOAT NOT NULL,
    close_price FLOAT NOT NULL,
    volume BIGINT NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    UNIQUE(stock_date, symbol)
);

SELECT symbol, round(avg(high_price),2) as avg_price
FROM stock_data
group by symbol
order by avg_price desc ;

SELECT symbol, MAX(volume) AS highest_volume
FROM stock_data
GROUP BY symbol
ORDER BY highest_volume DESC;

SELECT symbol, AVG(close_price) AS avg_close
FROM stock_data
GROUP BY symbol;

SELECT symbol, stock_date, volume
FROM stock_data
ORDER BY volume DESC
LIMIT 5;

SELECT symbol, MAX(close_price) AS max_close
FROM stock_data
GROUP BY symbol;
