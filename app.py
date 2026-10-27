import os
from flask import Flask, render_template, jsonify
app = Flask(__name__)
# Sample EV Market Summary Data
METRICS = {
    "total_models": 1250,
    "market_growth_pct": 84.5,
    "avg_range_miles": 324,
    "avg_battery_kwh": 78.4,
    "co2_offset_tons": "14.2M",
    "top_manufacturers": ["Tesla", "BYD", "Hyundai", "BMW", "Volkswagen"]
}
@app.route('/')
def home():
    """Main landing page featuring hero, live stats, tabbed embeds, and features."""
    return render_template("index.html", metrics=METRICS, active_page="home")
@app.route('/dashboard')
def dashboard():
    """Dedicated full-screen interactive Tableau Dashboard page."""
    return render_template("dashboard.html", metrics=METRICS, active_page="dashboard")
@app.route('/story')
def story():
    """Dedicated narrative walkthrough Tableau Story page."""
    return render_template("story.html", metrics=METRICS, active_page="story")
@app.route('/about')
def about():
    """Project documentation, methodology, and tech stack details."""
    return render_template("about.html", active_page="about")
@app.route('/api/stats')
def api_stats():
    """JSON API endpoint for dashboard summary metrics."""
    return jsonify({
        "status": "success",
        "data": METRICS
    })
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f" * EV Market Insights portal running at http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)