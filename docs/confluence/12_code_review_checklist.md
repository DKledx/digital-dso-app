### 📂 Cấu trúc thư mục `infra-deployments/`

```bash
infra-deployments/
├── environments/
│   ├── staging/
│   │   ├── kustomization.yaml
│   │   └── digital-dso-app.yaml
│   └── production/
│       ├── kustomization.yaml
│       └── digital-dso-app.yaml
├── README.md
```

---

### 📄 `environments/staging/digital-dso-app.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: digital-dso-app
  namespace: staging
spec:
  replicas: 1
  selector:
    matchLabels:
      app: digital-dso-app
  template:
    metadata:
      labels:
        app: digital-dso-app
    spec:
      containers:
        - name: app
          image: ghcr.io/your-org/digital-dso-app:v1.1.0
          ports:
            - containerPort: 8000
          envFrom:
            - configMapRef:
                name: digital-dso-app-config
            - secretRef:
                name: digital-dso-app-secret
```

---

### 📄 `environments/staging/kustomization.yaml`

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - digital-dso-app.yaml
```

---

### 📄 `README.md`

````markdown
# 🌐 GitOps Deployment – Digital DSO App

## Môi trường

- **Staging**: `environments/staging/`
- **Production**: `environments/production/`

## Cách hoạt động (ArgoCD hoặc FluxCD)

1. Theo dõi repo `infra-deployments`
2. Khi file YAML trong `staging/` hoặc `production/` được thay đổi (thường là image tag), ArgoCD sẽ tự động `sync`
3. Mỗi môi trường có thể apply thông qua `kustomization.yaml`

## Cập nhật image khi release

```bash
sed -i "s|image: .*|image: ghcr.io/your-org/digital-dso-app:v1.2.0|" environments/staging/digital-dso-app.yaml
git commit -am "Deploy v1.2.0"
git push
````

## Rollback

```bash
sed -i "s|image: .*|image: ghcr.io/your-org/digital-dso-app:v1.1.0|" environments/staging/digital-dso-app.yaml
git commit -am "Rollback to v1.1.0"
git push
```

## Gợi ý bổ sung

* Tạo `Service` + `Ingress` YAML để expose
* Tạo `ConfigMap` và `Secret` theo biến `.env`
* Dùng `sealed-secrets` nếu muốn mã hóa secret

