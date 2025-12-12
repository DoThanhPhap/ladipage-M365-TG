#!/bin/bash
# =============================================================================
# SCRIPT DEPLOY CHO MATBAO CLOUD HOSTING
# Domain: truonggiagp.com
# =============================================================================

# Cau hinh
DOMAIN="truonggiagp.com"
PROJECT_DIR=~/domains/$DOMAIN
VENV_PATH="/home/tru99077/virtualenv/domains/$DOMAIN/3.13/bin/activate"

echo "=== BAT DAU DEPLOY ==="

# Buoc 1: Di chuyen vao thu muc project
cd $PROJECT_DIR
echo "[1/6] Da vao thu muc: $PROJECT_DIR"

# Buoc 2: Tao file .env neu chua co
if [ ! -f ".env" ]; then
    echo "[2/6] Tao file .env..."
    cat > .env << 'EOF'
DEBUG=False
SECRET_KEY=django-insecure-truonggia-ms365-secretkey-2024-production
ALLOWED_HOSTS=truonggiagp.com,www.truonggiagp.com
CSRF_TRUSTED_ORIGINS=https://truonggiagp.com,https://www.truonggiagp.com
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EOF
    echo "[2/6] Da tao file .env"
else
    echo "[2/6] File .env da ton tai"
fi

# Buoc 3: Kich hoat virtualenv va cai dat dependencies
echo "[3/6] Cai dat dependencies..."
source $VENV_PATH
pip install -r requirements.txt --quiet

# Buoc 4: Collect static files
echo "[4/6] Collect static files..."
python manage.py collectstatic --noinput

# Buoc 5: Migrate database
echo "[5/6] Migrate database..."
python manage.py migrate --noinput

# Buoc 6: Tao symlink private_html cho SSL
echo "[6/6] Kiem tra symlink private_html..."
if [ ! -L ~/domains/$DOMAIN/private_html ]; then
    rm -rf ~/domains/$DOMAIN/private_html 2>/dev/null
    ln -s ~/domains/$DOMAIN/public_html ~/domains/$DOMAIN/private_html
    echo "[6/6] Da tao symlink private_html"
else
    echo "[6/6] Symlink private_html da ton tai"
fi

echo ""
echo "=== DEPLOY HOAN TAT ==="
echo "Hay vao DirectAdmin > Web Applications > RESTART de ap dung thay doi!"
echo ""
