const request = require('supertest')
const app = require('./index')

describe('Test Communication Service', () => {
    it('Should get health check route', async () => {
        const res = await request(app).get('/health-check')
        
        expect(res.status).toEqual(200)
        expect(res.body).toHaveProperty('message')
    })
    it('Test a post message', async () => {
        const res = await request(app)
        .post('/api/action')
        .send({host: 'vpn-sip.example.com.br', vpnAlternate: 'vpn-pico-a.example.com.br'})

        expect(204)
    })
})