# ReplicaSet

A ReplicaSet is defined with fields, including a selector that specifies how to identify Pods it can acquire, a number of replicas indicating how many Pods it should be maintaining, and a pod template specifying the data of new Pods it should create to meet the number of replicas criteria.

ReplicaSet then fulfills its purpose by creating and deleting Pods as needed to reach the desired number. When a ReplicaSet needs to create new Pods, it uses its Pod template.

In this case, it’s more or less the same as when we were creating the ReplicationController, except we’re using matchExpressions instead of label. 

```yaml
...
spec:
   replicas: 2
   selector:
     matchExpressions:
      - {key: app, operator: In, values: [guestbook, guest-book, guest_book]}
      - {key: env, operator: NotIn, values: [production]}
...
```

Now create the RS

```console
$ kubectl create -f frontend-rs.yaml
replicaset.apps/frontend created
```

Describe the RS

```console
$ kubectl describe replicaset.apps/frontend                                                                                                   
Name:         frontend
Namespace:    default
Selector:     app in (guest-book,guest_book,guestbook),env notin (production)
Labels:       app=guestbook-rs
              tier=frontend
Annotations:  <none>
Replicas:     2 current / 2 desired
Pods Status:  0 Running / 2 Waiting / 0 Succeeded / 0 Failed
Pod Template:
  Labels:  app=guestbook
           env=dev
  Containers:
   php-redis:
    Image:        gcr.io/google_samples/gb-frontend:v3
    Port:         <none>
    Host Port:    <none>
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Events:
  Type    Reason            Age   From                   Message
  ----    ------            ----  ----                   -------
  Normal  SuccessfulCreate  3s    replicaset-controller  Created pod: frontend-zdpgw
  Normal  SuccessfulCreate  3s    replicaset-controller  Created pod: frontend-r72q9
  ```

```console
$ kubectl get pods
NAME             READY   STATUS    RESTARTS   AGE
frontend-r72q9   1/1     Running   0          8m41s
frontend-zdpgw   1/1     Running   0          8m41s
```

Remove the RS

```console
$ kubectl delete -f  frontend-rs.yaml
replicaset.apps "frontend" deleted
```

