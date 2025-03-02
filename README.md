
# FlassTradingBoot

FlassTradingBoot is an advanced AI-driven trading bot designed to interact with multiple cryptocurrency exchanges and provide automated trading, subscription services, and a comprehensive dashboard for users. This project supports multiple payment gateways (Stripe, PayPal, Coinbase Commerce) and offers a referral system with rewards for inviting new users.

---

## Features

1. **Automated Trading**:
   - Supports multiple exchanges: Binance, Coinbase Pro, Kraken, KuCoin, Bitfinex, Huobi.
   - Uses AI algorithms for decision-making.
   - Customizable strategies.

2. **Subscription System**:
   - Flexible subscription plans.
   - Integrated payments via Stripe, PayPal, and Coinbase Commerce.

3. **Referral Program**:
   - Unique referral codes for each user.
   - Rewards: 1 free month for every 5 successful invites.

4. **Multi-language Support**:
   - English, Spanish, Romanian, and French.

5. **Live Chat**:
   - Integrated chat system for user communication.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/flassboot/flassboot.git
cd flassboot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory with the following content:

```
FLASK_ENV=production
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://user:password@localhost:5432/your_database
STRIPE_API_KEY=your_stripe_api_key
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_SECRET=your_paypal_secret
COINBASE_API_KEY=your_coinbase_api_key
```

### 4. Run Database Migrations

```bash
flask db upgrade
```

### 5. Start the Application

```bash
bash install.sh
```

---

## Usage

- Access the web interface at: `http://your-server-ip:5000`
- API available at: `http://your-server-ip:8000`

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License.

---

### Support

For support, contact: `support@flasstradingboot.com`
