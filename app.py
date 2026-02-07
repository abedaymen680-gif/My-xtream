from flask import Flask, jsonify, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "SNIPER Server is Running!"

@app.route('/player_api.php')
def xtream_api():
    u = request.args.get('username')
    p = request.args.get('password')
    action = request.args.get('action')

    # بيانات الدخول
    if u == "sniper" and p == "123":
        # طلب قائمة القنوات
        if action == "get_live_streams":
            return jsonify([{
                "num": 1,
                "name": "TF1 HD",
                "stream_id": 1000,
                "category_id": "1",
                "container_extension": "ts",
                "direct_source": "",
                "tv_archive": 0
            }])
        
        # طلب الأقسام
        if action == "get_live_categories":
            return jsonify([{"category_id": "1", "category_name": "SNIPER LIVE"}])

        # الرد الأساسي عند تسجيل الدخول (Login) - هذا هو الجزء الحساس
        return jsonify({
            "user_info": {
                "auth": 1,
                "status": "Active",
                "exp_date": "1999999999",
                "is_trial": "0",
                "active_cons": 0,
                "max_connections": 1,
                "allowed_output_formats": ["ts", "m3u8"]
            },
            "server_info": {
                "url": "my-iptv.onrender.com",
                "port": "80",
                "https_port": "443",
                "server_protocol": "http",
                "timezone": "Africa/Algiers",
                "timestamp_now": 1609459200
            }
        })
    
    return jsonify({"user_info": {"auth": 0}}), 200

@app.route('/live/<u>/<p>/<s_id>.ts')
def stream(u, p, s_id):
    if u == "sniper" and p == "123" and s_id == "1000":
        return redirect("http://41.205.93.154/TF1/mpegts")
    return "Error", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
  
