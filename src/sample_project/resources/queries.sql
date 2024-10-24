-- User related queries
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Get active users
SELECT id, username, email
FROM users
WHERE last_login >= NOW() - INTERVAL '30 days'
ORDER BY last_login DESC;

-- Product related queries
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INTEGER
);

-- Get low stock products
SELECT name, category, stock
FROM products
WHERE stock < 10
ORDER BY stock ASC;

-- Sales analysis
SELECT 
    category,
    COUNT(*) as total_sales,
    SUM(price * quantity) as revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;
