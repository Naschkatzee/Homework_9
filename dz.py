import asyncio
from asyncio import tasks
import httpx


async def get_users(client, url):
    resp = await client.get(url)
    users = resp.json()
    return users


async def main():
    async with httpx.AsyncClient() as client:

        tasks = []

        for number in range(1, 11):

            url = f'https://jsonplaceholder.typicode.com/users/{number}/posts'
            tasks.append(asyncio.ensure_future(get_users(client, url)))
            url = f'https://jsonplaceholder.typicode.com/users/{number}/todos'
            tasks.append(asyncio.ensure_future(get_users(client, url)))
            url = f'https://jsonplaceholder.typicode.com/users/{number}/albums'

            # url = f'https://jsonplaceholder.typicode.com/users/{number}/posts'
            tasks.append(asyncio.ensure_future(get_users(client, url)))

        users = await asyncio.gather(*tasks)
        for user in users:
            print(user)

if __name__ == '__main__':
    asyncio.run(main())
